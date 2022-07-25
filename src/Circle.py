import math

from src.Figure import Figure


class Circle(Figure):
    """circle class"""
    name = 'CIRCLE'

    def __init__(self, radius):
        """constructor"""
        self.r = radius

    @property
    def circle_circumference(self):
        """circle circumference function"""
        return self.r * 2 + math.pi

    @property
    def circle_area(self):
        """circle area function"""
        return self.r ** 2 * math.pi

# r = float(input('Enter the radius of the circle: '))
# x = Circle(r)

# print('The circumference is = {}, The area of the circle is = {}'.format(x.circle_ring(),
#                                                                          x.circle_area()))