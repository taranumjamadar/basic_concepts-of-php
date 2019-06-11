def circle(r):
    """Return area and perimeter of circle given radius r"""
    pi = 3.14
    area = pi*r*r
    perimeter = 2*pi*r
    return area, perimeter
    
    circle(4)
    a,p = circle(6)