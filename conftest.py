import pytest

from src.Triangle import Triangle


@pytest.fixture
def positive_triangle():
    return Triangle(13, 14, 15)
