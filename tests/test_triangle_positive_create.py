def test_triangle_positive_create(positive_triangle):
    """positive triangle creation test"""
    assert positive_triangle.perimeter == 42
    assert positive_triangle.area == 84
