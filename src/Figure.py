class Figure:
    """figure class"""
    name = None

    @property
    def area(self):
        """area function"""
        return None

    @property
    def perimeter(self):
        """perimeter function"""
        return None

    def add_area(self, figure):
        if not isinstance(figure):
            raise ValueError('Not a geometric figure.')
        return self.area + figure.area
