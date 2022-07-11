import pytest
from app.function import add


@pytest.mark.parametrize('value, result',
                         [
                             ((7, 3), 10),
                             (('test ', 'string'), 'test string'),
                             ((11.1, 9.9), 21)
                         ]
                         )
def test_sum(value, result):
    assert add(*value) == result
