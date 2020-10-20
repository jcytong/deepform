"""Create token data for each of the pdfs (or directories of pdfs) passed in."""


import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd
import pdfplumber
from tqdm import tqdm

from deepform.common import PDF_DIR, TOKEN_DIR
from deepform.data.add_features import add_base_features
from deepform.document import FEATURE_COLS, Document
from deepform.logger import logger
from deepform.pdfs import get_pdf_path


def tokenize_pdf(pdf_path):
    """Return a DataFrame of document token data for a pdf at the input path."""
    pages = []
    for i, page in enumerate(pdfplumber.open(pdf_path).pages):
        df = pd.DataFrame(page.extract_words())
        if df.empty:
            continue
        df["page"] = i
        df["page"] = df["page"].astype("i2")
        df["x0"] = df["x0"].astype("f4")
        df["y0"] = df["top"].astype("f4")
        df["x1"] = df["x1"].astype("f4")
        df["y1"] = df["bottom"].astype("f4")
        df["token"] = df["text"].astype("string")
        pages.append(df[["page", "x0", "y0", "x1", "y1", "token"]])
    if not pages:
        raise EOFError(f"No tokens found in {pdf_path}")
    return pd.concat(pages).reset_index(drop=True)


def create_token_doc(pdf_path, token_dir=TOKEN_DIR, overwrite=False):
    pdf_path, token_dir = Path(pdf_path), Path(token_dir)
    assert pdf_path.is_file() and pdf_path.suffix == ".pdf"

    slug = pdf_path.stem
    token_path = token_dir / f"{slug}.parquet"
    if token_path.is_file():
        if overwrite:
            logger.warning(f"Overwriting {token_path}")
        else:
            return

    try:
        tokens = tokenize_pdf(pdf_path)
    except EOFError:
        logger.warning(f"pdfplumber found no tokens in '{pdf_path}'")
        return
    except Exception as e:
        logger.error(f"Unable to tokenize {pdf_path}: {e}")
        return

    token_dir.mkdir(parents=True, exist_ok=True)
    tokens.to_parquet(token_path)
    return token_path


def pdf_paths(*paths):
    for path in paths:
        path = Path(path)
        if path.is_file():
            if path.suffix != ".pdf":
                logger.warning(f"Skipping non-pdf '{path}'")
                continue
            yield path
        elif path.is_dir():
            for file_path in path.glob("*.pdf"):
                yield file_path
        else:
            logger.warning(f"'{path}' is not a file or directory")


def create_token_docs_from_pdfs(*paths, overwrite=False):

    with ThreadPoolExecutor() as executor:
        pdf_files = list(pdf_paths(*paths))
        print(f"Tokenizing {len(pdf_files):,} pdfs...")
        results = list(
            tqdm(executor.map(create_token_doc, pdf_files), total=len(pdf_files))
        )

    tokenized = [p for p in results if p]
    print(f"Tokenized {len(tokenized)} documents.")
    return tokenized


def create_token_docs_from_slugs(slugs, token_dir=TOKEN_DIR):
    def tokenize(slug):
        pdf_file = get_pdf_path(slug)
        return create_token_doc(pdf_file, token_dir=token_dir)

    with ThreadPoolExecutor() as executor:
        print(f"Acquiring and tokenizing {len(slugs):,} documents...")
        results = list(tqdm(executor.map(tokenize, slugs), total=len(slugs)))

    tokenized = [p for p in results if p]
    print(f"Tokenized {len(tokenized)} documents.")
    return tokenized


def extract_doc(pdf_path, window_len):
    """Create a Document with features extracted from a pdf."""
    pdf_path = Path(pdf_path)
    tokens = tokenize_pdf(pdf_path)
    # Remove tokens shorter than three characters.
    df = tokens[tokens["token"].str.len() >= 3]
    df = add_base_features(df)
    df["tok_id"] = np.minimum(511, df["tok_id"])
    return Document(
        slug=pdf_path.stem,
        tokens=df,
        features=df[FEATURE_COLS].to_numpy(dtype=float),
        labels=np.zeros(len(df), dtype=bool),  # Dummy.
        positive_windows=np.array(0),  # Dummy.
        window_len=window_len,
        label_values={},
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-f",
        "--force",
        type=bool,
        default=False,
        help="overwrite existing token files",
    )
    parser.add_argument(
        "pdf",
        nargs="?",
        default=PDF_DIR,
        help="pdf or directory of pdfs to process",
    )
    parser.add_argument("--log-level", dest="log_level", default="ERROR")
    args = parser.parse_args()
    logger.setLevel(args.log_level.upper())

    create_token_docs_from_pdfs(args.pdf, overwrite=args.force)
