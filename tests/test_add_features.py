import pandas as pd

from deepform.data.add_features import (
    extend_and_write_docs,
    fraction_digits,
    pq_index_and_dir,
)
from deepform.data.create_vocabulary import get_token_id
from deepform.data.csv_to_parquet import CSV_COL_TYPES
from deepform.util import is_dollar_amount, log_dollar_amount
from test_csv_to_parquet import training_docs_data


def test_convert_csv_to_parquet(faker, tmp_path):
    num_docs = 5

    idx_path = tmp_path / "doc_index.parquet"
    idx_path, pq_path = pq_index_and_dir(idx_path)

    # Create the source data to start with.
    df = training_docs_data(faker, num_docs, repeat=False)
    df = df.astype(CSV_COL_TYPES)

    # Run the conversion code.
    extend_and_write_docs(df, idx_path)

    # Check out the index.
    index = pd.read_parquet(idx_path)

    assert len(index) == num_docs
    assert set(df.slug) == set(index.index)

    # Check out each individual document that was produced.
    for slug, length, best_match in index.itertuples():
        doc = pd.read_parquet(pq_path / f"{slug}.parquet")
        # Doc features
        assert doc.token.str.len().min() >= 3
        assert length == len(doc)
        assert best_match == doc.gross_amount.max()
        # Row features
        assert (doc.tok_id == doc.token.apply(get_token_id)).all()
        assert (doc.length == doc.token.str.len()).all()
        assert (doc.digitness == doc.token.apply(fraction_digits)).all()
        assert (doc.is_dollar == doc.token.apply(is_dollar_amount)).all()
        assert (doc.log_amount == doc.token.apply(log_dollar_amount).fillna(0)).all()
