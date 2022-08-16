def test_add_area_positive(positive_triangle, positive_circle):
    """valid addition of the areas of a triangle and a circle"""
    triangle = positive_triangle
    circle = positive_circle
    return triangle.add_area(circle)
