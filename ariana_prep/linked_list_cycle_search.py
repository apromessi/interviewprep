#!/usr/bin/env python


class LinkedListItem(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return 'value: {}'.format(self.value)


class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def add_to_head(self, value):
        new_head = LinkedListItem(value, self.head)
        self.head = new_head
        return self.head

    def remove_from_head(self):
        if not self.head.next:
            return None

        self.head = self.head.next
        # or return the item that was removed?
        return self.head

    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def remove_item(self, value):
        prev_node = None
        current_node = self.head
        num_instances_removed = 0

        # consider ways to make this cleaner
        while current_node:
            if current_node.value == value:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.remove_from_head()
                    prev_node = current_node

                num_instances_removed += 1
            else:
                prev_node = current_node

            current_node = current_node.next

        print('found and removed {} instances'.format(num_instances_removed))

    def find_tail(self):
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        return current_node


# test utility
def create_cyclical_linked_list(linked_list):
    if not linked_list.head.next:
        linked_list.add_to_head('new_head')

    tail_node = linked_list.find_tail()
    tail_node.next = linked_list.head


def has_cycle(linked_list):
    has_cycle = False
    current_node = linked_list.head

    while current_node.next and has_cycle is False:
        if current_node.next == linked_list.head:
            has_cycle = True
        current_node = current_node.next

    return has_cycle


def main():
    linked_list = LinkedList(LinkedListItem(1))
    print(has_cycle(linked_list), 'should be False')

    my_list = [7, 5, 3, 9, 0, 3, 1, 2, 'b', 'a', 'c']
    for item in my_list:
        linked_list.add_to_head(item)
    print(has_cycle(linked_list), 'should be False')

    create_cyclical_linked_list(linked_list)
    print(has_cycle(linked_list), 'should be True')

if __name__ == '__main__':
    main()
