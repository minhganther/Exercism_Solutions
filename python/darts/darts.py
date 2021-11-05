def score(x, y):

    coord_val = x**2 + y**2
    if coord_val <= 1:
        return 10
    elif coord_val <= 25:
        return 5
    elif coord_val <= 100:
        return 1
    return 0
