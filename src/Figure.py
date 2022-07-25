class Figure:
    """figure class"""
    name = None

    @property
    def perimeter(self) -> float:
        """perimeter function"""
        return None

    @property
    def area(self) -> float:
        """area function"""
        return None

    def add_perimeter(self, figure):
        """perimeter addition"""
        if not isinstance(figure, Figure):
            raise ValueError('Not a geometric figure.')
        return self.perimeter + figure.perimeter

    def add_area(self, figure):
        """area addition"""
        if not isinstance(figure, Figure):
            raise ValueError('Not a geometric figure.')
        return self.area + figure.area
