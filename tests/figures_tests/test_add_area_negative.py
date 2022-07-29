import pytest


def test_add_area_negative(positive_triangle):
    """invalid addition of the areas of a triangle and a circle"""
    with pytest.raises(ValueError):
        return positive_triangle.add_area(55)
