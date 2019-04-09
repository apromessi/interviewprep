#!/usr/bin/env python


class Queue(object):
    def __init__(self, queue=[]):
        self.queue = queue

    def add(self, x):
        self.queue.append(x)
        return self.queue

    def remove(self):
        if not self.queue:
            return None

        removed = self.queue[0]
        self.queue = self.queue[1:]
        return removed, self.queue


def main():
    my_queue = Queue([1, 3, 4, 5])
    print(my_queue.remove())
    print(my_queue.add(9))
    print(my_queue.queue)

if __name__ == '__main__':
    main()
