def score(x, y):

    """ Determine whether a dart with the coordinates x,y is contained within a     certain concentric circle and give points according to that.

    The solution is based on the pythagorean equation a^2 + b^2 = c^2 with x and    y being the sides of the triangle and r the hypothenuse.
    """
    coord_val = x**2 + y**2
    if coord_val <= 1:
        return 10
    elif coord_val <= 25:
        return 5
    elif coord_val <= 100:
        return 1
    return 0
