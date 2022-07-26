import pytest

from src.Triangle import Triangle
from src.Circle import Circle
from src.Square import Square
from src.Rectangle import Rectangle


@pytest.fixture
def positive_triangle():
    """for the positive triangle creation test"""
    return Triangle(13, 14, 15)


@pytest.fixture
def positive_circle():
    """for the positive circle creation test"""
    return Circle(13)


@pytest.fixture
def positive_square():
    """for the positive square creation test"""
    return Square(17)


@pytest.fixture
def positive_rectangle():
    """for the positive rectangle creation test"""
    return Rectangle(33, 71)
