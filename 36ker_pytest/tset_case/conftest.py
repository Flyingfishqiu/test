import pytest


@pytest.fixture(scope='function')
def fix():
    print('fix')