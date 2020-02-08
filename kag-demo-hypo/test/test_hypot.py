from hypothesis import given, strategies
from hypothesis.extra.pandas import column, data_frames

from conftest import raw_

import kag

def hypot_df_generator():
    df = raw_()
    cols = []
    for col in ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q8', 'Q9']:
        cols.append(column(col, elements=strategies.sampled_from(df[col].unique())))
    return data_frames(columns=cols)


@given(hypot_df_generator())
def test_countries(gen_df):
    if gen_df.shape[0] == 0:
        return
    kag_ = kag.tweak_kag(gen_df)
    assert len(kag_.Country.unique()) <= 4

