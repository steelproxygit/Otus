import math

from src.Figure import Figure


class Triangle(Figure):
    """triangle class"""
    name = 'TRIANGLE'

    def __init__(self, side_1, side_2, side_3):
        """constructor"""
        self.s1 = side_1
        self.s2 = side_2
        self.s3 = side_3
        if side_1 + side_2 <= side_3 or side_1 + side_3 <= side_2 or side_2 + side_3 <= side_1:
            raise ValueError('Unable to create a triangle. Incorrect side values.')

    @property
    def perimeter(self):
        """triangle perimeter function"""
        return self.s1 + self.s2 + self.s3

    @property
    def area(self):
        """triangle area function"""
        p = self.perimeter / 2
        return float('%.6f' % math.sqrt(p * (p - self.s1) * (p - self.s2) * (p - self.s3)))

# a = float(input('Enter the first side of the triangle: '))
# b = float(input('Enter the second side of the triangle: '))
# c = float(input('Enter the third side of the triangle: '))
# x = Triangle(a, b, c)

# print(Triangle.name)
# print('The perimeter of the triangle is = {}, The area of the triangle is = {}'.format(x.perimeter(),
#                                                                                        x.area()))
