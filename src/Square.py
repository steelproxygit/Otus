from src.Figure import Figure


class Square(Figure):
    """square class"""
    name = 'SQUARE'

    def __init__(self, side):
        """constructor"""
        self.s = side

    @property
    def perimeter(self):
        """square perimeter function"""
        return 4 * self.s

    @property
    def area(self):
        """triangle area function"""
        return self.s * self.s

# s = float(input('Enter the side of the square: '))
# x = Square(s)

# print(Square.name)
# print('The perimeter of the square is = {}, The area of the square is = {}'.format(x.perimeter(),
#                                                                                    x.area()))
