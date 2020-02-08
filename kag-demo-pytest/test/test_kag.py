import pytest

import kag


@pytest.fixture(scope='session')
def df():
    df = kag.load_raw('data/kaggle-survey-2018.zip')
    return kag.tweak_kag(df)


def test_salary_mean(df):
    assert 10_000 < df.Salary.mean() < 100_000

def test_salary_between(df):
    assert df.Salary.min() >= 0
    assert df.Salary.max() <= 500_000

def test_salary_not_null(df):
    assert not df.Salary.isna().any()

def test_country_values(df):
    assert set(df.Country.unique()) == {'Another', 'United States of America', 'India', 'China'}

def test_salary_dtype(df):
    assert df.Salary.dtype == int
