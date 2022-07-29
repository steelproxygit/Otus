from src.Figure import Figure


class Rectangle(Figure):
    """rectangle class"""
    name = 'RECTANGLE'

    def __init__(self, width, height):
        """constructor"""
        self.w = width
        self.h = height

    @property
    def perimeter(self):
        """rectangle perimeter function"""
        return 2 * (self.w + self.h)

    @property
    def area(self):
        """rectangle area function"""
        return self.w * self.h

# w = float(input('Enter the width of the rectangle: '))
# h = float(input('Enter the height of the rectangle: '))
# x = Rectangle(w, h)

# print(Rectangle.name)
# print('The perimeter of the rectangle is = {}, The area of the rectangle is = {}'.format(x.perimeter,
#                                                                                          x.area))
