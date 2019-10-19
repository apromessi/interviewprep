#!/usr/bin/env python


class Stack(object):
    def __init__(self, stack=[]):
        self.stack = stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return None

        return self.stack.pop(-1)

    def peek(self):
        if not self.stack:
            return None

        return self.stack[-1]


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    my_stack = Stack(my_list)
    print my_stack.stack

    my_stack.push(10)
    print my_stack.stack

    print my_stack.peek()
    print my_stack.stack

    print my_stack.pop()
    print my_stack.stack