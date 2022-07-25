import pytest

from src.Triangle import Triangle


def test_triangle_negative_create():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)
