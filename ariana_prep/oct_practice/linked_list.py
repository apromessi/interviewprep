#!/usr/bin/env python


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return 'value: {}'.format(self.value)


class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def add_to_head(self, value):
        new_head = Node(value, self.head)
        self.head = new_head

    def remove_from_head(self):
        if self.head.next:
            self.head = self.head.next
        else:
            self.head.value = None

    def show(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print ' -> '.join(values)

    def remove_item(self, value):
        if self.head.value == value:
            self.remove_from_head()
        else:
            prev = self.head
            current = self.head.next
            while current:
                if current.value == value:
                    prev.next = current.next
                    current.next = None
                    break
                else:
                    prev = current
                    current = current.next


if __name__ == '__main__':
    new_node = Node(1)

    print new_node

    linked_list = LinkedList(new_node)
    linked_list.show()
    linked_list.add_to_head(2)
    linked_list.add_to_head(3)
    linked_list.add_to_head(4)
    linked_list.show()

    print 'testing remove item'
    linked_list.remove_item(3)
    linked_list.show()
    linked_list.remove_item(4)
    linked_list.show()
    linked_list.remove_item(1)
    linked_list.show()

    print 'testing remove from head'
    linked_list.add_to_head(2)
    linked_list.remove_from_head()
    linked_list.show()

    linked_list.remove_from_head()
    linked_list.show()

