"""Determine the type of a triangle"""

def equilateral(sides):
    sides.sort()
    return sides[0] == sides[1]  == sides[2] and 0 not in sides and sides[0]+sides[1]>sides[2]


def isosceles(sides):
    sides.sort()
    return (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]) and 0 not in sides and sides[0]+sides[1]>sides[2]


def scalene(sides):
    sides.sort()
    return not equilateral(sides) and not isosceles(sides) and sides[0]+sides[1]>sides[2]
