# A left rotation operation on an array shifts each of the array's
# elements 1 unit to the left. For example, if 2 left rotations are
# performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].

# Given an array a of n integers and a number, d, perform  left rotations
# on the array. Return the updated array to be printed as a single line of
# space-separated integers.

def rotLeft(a, d):
    numbers_to_rotate = d % len(a)
    l1 = a[:numbers_to_rotate]
    l2 = a[numbers_to_rotate:]

    rotated = l2 + l1
    return rotated