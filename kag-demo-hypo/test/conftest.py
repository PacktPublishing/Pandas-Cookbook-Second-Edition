import pytest

import kag

@pytest.fixture(scope='session')
def raw():
    return raw_()

def raw_():
    return kag.load_raw('data/kaggle-survey-2018.zip')

@pytest.fixture(scope='session')
def df(raw):
    return kag.tweak_kag(raw)
    
