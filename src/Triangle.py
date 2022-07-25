import math

from src.Figure import Figure


class Triangle(Figure):
    """triangle class"""
    name = 'TRIANGLE'

    def __init__(self, side1, side2, side3):
        """constructor"""
        self.s1 = side1
        self.s2 = side2
        self.s3 = side3
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise ValueError('Unable to create a triangle. Incorrect side values.')

    @property
    def triangle_perimeter(self):
        """triangle perimeter function"""
        return self.s1 + self.s2 + self.s3

    @property
    def triangle_area(self):
        """triangle area function"""
        p = self.triangle_perimeter() / 2
        return float('%.6f' % math.sqrt(p * (p - self.s1) * (p - self.s2) * (p - self.s3)))

# a = float(input('enter the first side of the triangle: '))
# b = float(input('enter the second side of the triangle: '))
# c = float(input('enter the third side of the triangle: '))
# x = Triangle(a, b, c)

# print(Triangle.name)
# print('the perimeter of the triangle is = {}, the area of the triangle is = {}'.format(x.triangle_perimeter(),
#                                                                                        x.triangle_area()))
