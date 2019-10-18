#!/usr/bin/env python

from ordered_stack import OrderedStack

def make_towers(n):
    """
    Given a number, n, creates and returns three spindles (as ordered stacks).
    The first spindle contains n disks, while the other two are empty.
    """
    spindle_1 = OrderedStack()
    spindle_2 = OrderedStack()
    spindle_3 = OrderedStack()

    numbers = reversed(range(1, n+1))
    for x in numbers:
        spindle_1.push(x)

    return spindle_1, spindle_2, spindle_3

def hanoi(source, spare, target):
    if len(source.stack) > 1:
        return hanoi(spare, source, target)
    else:
        largest_disk = source.pop()
        target.push(largest_disk)

def main():
    spindle_1, spindle_2, spindle_3 = make_towers(5)
    print(spindle_1)
    print(spindle_2)
    print(spindle_3)
    hanoi(spindle_1, spindle_2, spindle_3)
    print(spindle_1)
    print(spindle_2)
    print(spindle_3)

if __name__ == '__main__':
    main()
