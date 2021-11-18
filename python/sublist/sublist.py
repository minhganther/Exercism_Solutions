"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def sublist(list_one, list_two):
    list1 = ",".join([str(i) for i in list_one])
    list2 = ",".join([str(i) for i in list_two])

    if list1==list2:
        return EQUAL
    elif list1 in list2 and all(i in list_two for i in list_one):
        return SUBLIST
    elif list2 in list1 and all(i in list_one for i in list_two):
        return SUPERLIST
    return UNEQUAL
