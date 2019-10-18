#!/usr/bin/env python


class OrderedStack(object):
    def __init__(self):
        self.stack = [] 

    def push(self, x):
        if self.peek() is None:
            return self.stack.append(x)

        if x < self.peek():
            return self.stack.append(x)
        else:
            raise Exception
            print('Error: cannot push')

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

    def __repr__(self):
        return '{}'.format(self.stack)


def main():
    my_stack = OrderedStack()
    print(my_stack.peek())
    my_stack.push(1)
    print(my_stack.peek())
    my_stack.push(5)
    print(my_stack.peek())
    my_stack.push(3)
    print(my_stack.peek())
    print(my_stack)

if __name__ == '__main__':
    main()
