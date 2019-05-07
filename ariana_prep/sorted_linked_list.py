#!/usr/bin/env Python


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return 'Value: {}'.format(self.value)


class SortedLinkedList(object):
    def __init__(self, head):
        self.head = head

    def show(self):
        """
        Print out the nodes in the linked list (skipping the head).
        """
        current = self.head
        to_print = ''

        while current.next:
            current = current.next
            to_print += '{} -> '.format(current.value)
        print to_print

    def insert(self, value):
        """
        Takes a number, creates a new Node containing that number, and adds
        it to the list in the correct position, returning the Node that was
        created. A number that already exists in the list should be inserted
        before the first existing Node with that value.
        """
        new_node = Node(value)
        insert_pt = self.insert_pt(value)

        if insert_pt.next:
            new_node.next = insert_pt.next
        insert_pt.next = new_node

        return new_node

    def find(self, value):
        """
        Takes a number and finds the first Node in the list whose elem is that
        number. If no such node exists, returns null.
        """
        insert_pt = self.insert_pt(value)

        if insert_pt.next and insert_pt.next.value == value:
            return insert_pt.next
        else:
            return None

    def remove(self, value):
        """
        Takes a number and removes the first Node in the list whose elem is that
        number. If no such node exists, does nothing.
        """
        insert_pt = self.insert_pt(value)

        if insert_pt.next and insert_pt.next.value == value:
            to_remove = insert_pt.next
            if to_remove.next:
                insert_pt.next = to_remove.next
            else:
                insert_pt.next = None

    def insert_pt(self, value):
        """
        Takes a number and finds the Node in the list after which the number would
        be inserted. Used as a helper function to implement the step "find where [X]
        would be" in each of the other operations.
        """
        # return node that would take a new node with 'value' as its next
        current = self.head

        while current.next and current.next.value < value:
            current = current.next

        return current


def merge_sort_linked_list(linked_list1, linked_list2):
    pass


def main():
    head = Node('H')
    linked_list = SortedLinkedList(head)

    linked_list.insert(5)
    linked_list.show()
    linked_list.insert(2)
    linked_list.show()
    linked_list.insert(7)
    linked_list.show()
    print(linked_list.find(5))
    print(linked_list.find(1))
    print(linked_list.find(9))
    linked_list.remove(1)
    linked_list.show()

if __name__ == '__main__':
    main()
