from src.Figure import Figure


class Square(Figure):
    """square class"""
    name = 'SQUARE'

    def __init__(self, side):
        """constructor"""
        self.side = side

    @property
    def square_perimeter(self):
        """square perimeter function"""
        return 4 * self.side

    @property
    def square_area(self):
        """triangle area function"""
        return self.side * self.side

# s = float(input('Enter the side of the square: '))
# x = Square(s)

# print(Square.name)
# print('The perimeter of the square is = {}, The area of the square is = {}'.format(x.square_perimeter(),
#                                                                                    x.square_area()))
