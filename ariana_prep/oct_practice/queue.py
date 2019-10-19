#!/usr/bin/env python


class Queue(object):
    def __init__(self, queue=[]):
        self.queue = queue

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.queue:
            return None

        return self.queue.pop(0)


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    my_queue = Queue(my_list)
    print my_queue.queue

    my_queue.push(10)
    print my_queue.queue

    print my_queue.pop()
    print my_queue.queue

    my_queue = Queue()
    print my_queue.pop()
    my_queue.push(1)
    print my_queue.queue