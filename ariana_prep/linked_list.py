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


def main():
    my_linked_list = LinkedList(LinkedListItem(1))
    print(my_linked_list.head)
    print(my_linked_list.add_to_head(2))
    print(my_linked_list.add_to_head(3))
    print(my_linked_list.add_to_head(4))
    print(my_linked_list.add_to_head(5))
    print(my_linked_list.add_to_head(4))
    print(my_linked_list.add_to_head(4))
    print(my_linked_list.add_to_head(4))
    print(my_linked_list.remove_from_head())
    my_linked_list.show()

    print(my_linked_list.remove_item(1))
    my_linked_list.show()

if __name__ == '__main__':
    main()

# quick to add and remove items at the head. O(n) to do most other things
# (show all items, add or remove items from tail, search for a certain item
# or a remove an instance)
