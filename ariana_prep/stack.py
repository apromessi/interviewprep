#!/usr/bin/env python


class Stack(object):
    def __init__(self, stack=[]):
        self.stack = stack

    def push(self, x):
        return self.stack.append(x)

    def pop(self):
        if not self.stack:
            return None

        popped = self.stack[-1]
        self.stack = self.stack[:-1]

        return popped

    def peek(self):
        if not self.stack:
            return None

        return self.stack[-1]


def main():
    my_stack = Stack()
    print(my_stack.peek())

if __name__ == '__main__':
    main()
