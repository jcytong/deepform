"""
Process a parquet of all training data to add labels and computed features.

Final data is stored individually (per-document) to enable random access of
small samples, with an index over all the documents.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from enum import Enum, auto
from pathlib import Path

import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
from tqdm import tqdm

from deepform.common import DATA_DIR, TOKEN_DIR, TRAINING_DIR, TRAINING_INDEX
from deepform.data.create_vocabulary import get_token_id
from deepform.logger import logger
from deepform.util import (
    date_similarity,
    default_similarity,
    dollar_similarity,
    is_dollar_amount,
    log_dollar_amount,
)


class TokenType(Enum):
    NONE = 0
    CONTRACT_NUM = auto()
    ADVERTISER = auto()
    FLIGHT_FROM = auto()
    FLIGHT_TO = auto()
    GROSS_AMOUNT = auto()


LABEL_COLS = {
    # Each label column, and the match function that it uses.
    "contract_num": default_similarity,
    "advertiser": default_similarity,
    "flight_from": date_similarity,
    "flight_to": date_similarity,
    "gross_amount": dollar_similarity,
}


def extend_and_write_docs(source_dir, manifest, pq_index, out_path):
    """Split data into individual documents, add features, and write to parquet."""

    token_files = {p.stem: p for p in source_dir.glob("*.parquet")}

    jobqueue = []
    for row in manifest.itertuples():
        slug = row.file_id
        if slug not in token_files:
            logger.error(f"No token file for {slug}")
            continue
        labels = {}
        for label_col in LABEL_COLS:
            labels[label_col] = getattr(row, label_col)
            if not labels[label_col]:
                logger.warning(f"'{label_col}' for {slug} is empty")
        jobqueue.append(
            {
                "token_file": token_files[slug],
                "dest_file": out_path / f"{slug}.parquet",
                "labels": labels,
            }
        )

    # Spin up a bunch of jobs to do the conversion
    with ThreadPoolExecutor() as executor:
        doc_jobs = []
        for kwargs in jobqueue:
            doc_jobs.append(executor.submit(process_document_tokens, **kwargs))

        logger.debug("Waiting for jobs to complete")
        progress = tqdm(as_completed(doc_jobs), total=len(doc_jobs))
        doc_results = [j.result() for j in progress]

    logger.debug(f"Writing document index to {pq_index}...")
    doc_index = pd.DataFrame(doc_results).set_index("slug", drop=True)
    doc_index.to_parquet(pq_index, compression="lz4")


def pq_index_and_dir(pq_index, pq_path=None):
    """Get directory for sharded training data, creating if necessary."""
    pq_index = Path(pq_index).resolve()
    if pq_path is None:
        pq_path = TRAINING_DIR
    else:
        pq_path = Path(pq_path)
    pq_index.parent.mkdir(parents=True, exist_ok=True)
    pq_path.mkdir(parents=True, exist_ok=True)
    return pq_index, pq_path


def process_document_tokens(token_file, dest_file, labels):
    """Filter out short tokens, add computed features, and return index info."""
    slug = token_file.stem
    doc = pd.read_parquet(token_file)

    doc = label_tokens(doc, labels)

    # Strip whitespace off all tokens.
    doc["token"] = doc.token.str.strip()

    # Remove tokens shorter than three characters.
    doc = doc[doc.token.str.len() >= 3]

    # Extend with the straightforward features.
    doc = add_base_features(doc)

    # Handle the features that need the whole document.
    doc["label"] = np.zeros(len(doc), dtype="u1")
    # The "label" column stores the TokenType that correctly labels this token.
    # By default this is 0, or "NONE".
    best_matches = {}
    for feature in LABEL_COLS:
        token_value = TokenType[feature.upper()].value
        max_score = doc[feature].max()
        best_matches[f"best_match_{feature}"] = max_score
        matches = token_value * np.isclose(doc[feature], max_score)
        doc["label"] = np.maximum(doc["label"], matches)

    # Write to its final location.
    doc.to_parquet(dest_file, compression="lz4", index=False)

    # Return the summary information about the document.
    return {"slug": slug, "length": len(doc), **labels, **best_matches}

## This is the function as it currently exists:
def label_tokens(tokens, labels, n):
    for col_name, label_value in labels.items():
        tokens[col_name] = 0.0
        match_fn = LABEL_COLS[col_name]

    # Assemble all the token strings that can be formed for a token at a specific index with maximum n-gram length of n
        for index, token in tokens.token.items():  
            n_grams = []
            match_percentages = []
            for x in range(1,n+1): # x is all the possible lengths of n-gram
                for y in range (1, x+1): # y is all the possible index modifications for that length of n-gram
                    n_gram = doc.loc[index-y+1:index-y+x, "token"].values.tolist()   
                    n_gram = ''.join(n_gram)
                    n_grams.append(n_gram)

        # Calculate the match percentage for each of them using the correct match_fn
            match_percentages = [match_fn(label_value, match) for match in n_grams]

        # Take the maximum value from match_percentages
            best_match = max(match_percentages)

        #Add that value to the tokens column at the correct index
            tokens.loc[index,col_name] = best_match
    return tokens

## Need to rewrite it with the following capacities: 
def label_tokens(tokens, labels):
    """
    tokens is a 
    """
    # in here we need to add n (the maximum number of possible tokens in the target)
    n = 5
    # in here we need to compile a series of n possible answer sets.  
    for col_name, label_value in labels.items():
        match_fn = LABEL_COLS[col_name] # Gets us the particular match function to use for this type of data
        tokens[col_name] = tokens.token.apply(match_fn, args=(label_value,)) #Applies the match function to the label value and ""  <<? 
    # each token has to have only one value assigned to it rather than (N + N-1 + N-2 + ... + n-N).  So we're going to need a max function here. 
    return tokens # Confirm this returns the entire set of tokens.



def fraction_digits(s):
    """Return the fraction of a string that is composed of digits."""
    return np.mean([c.isdigit() for c in s]) if isinstance(s, str) else 0.0


def match_string(a, b):
    m = fuzz.ratio(a.lower(), b.lower()) / 100.0
    return m if m >= 0.9 else 0


def add_base_features(token_df):
    """Extend a DataFrame with features that can be pre-computed."""
    df = token_df.copy()
    df["tok_id"] = df["token"].apply(get_token_id).astype("u2")
    df["length"] = df["token"].str.len().astype("i2")
    df["digitness"] = df["token"].apply(fraction_digits).astype("f4")
    df["is_dollar"] = df["token"].apply(is_dollar_amount).astype("f4")
    df["log_amount"] = df["token"].apply(log_dollar_amount).fillna(0).astype("f4")

    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", help="CSV with labels for each document", default = DATA_DIR / "3_year_manifest.csv")
    parser.add_argument(
        "indir",
        nargs="?",
        default=TOKEN_DIR,
        help="directory of document tokens",
    )
    parser.add_argument(
        "indexfile",
        nargs="?",
        default=TRAINING_INDEX,
        help="path to index of resulting parquet files",
    )
    parser.add_argument(
        "outdir",
        nargs="?",
        default=TRAINING_DIR,
        help="directory of parquet files",
    )
    parser.add_argument("--log-level", dest="log_level", default="INFO")
    args = parser.parse_args()
    logger.setLevel(args.log_level.upper())

    logger.info(f"Reading {Path(args.manifest).resolve()}")
    manifest = pd.read_csv(args.manifest)

    indir, index, outdir = Path(args.indir), Path(args.indexfile), Path(args.outdir)
    index.parent.mkdir(parents=True, exist_ok=True)
    outdir.mkdir(parents=True, exist_ok=True)
    extend_and_write_docs(indir, manifest, index, outdir)
