#!/usr/bin/env python

from hash_table import HashTable, HASHING_CONSTANT
from random import shuffle


class Set(HashTable):
    def add(self, key):
        self.insert(key, None)

    def contains(self, key):
        index = hash(key)
        key_value = self.get_key_value_at_index(key, index)
        if key_value:
            return True
        return False

    def pop(self):
        indices = [x for x in range(HASHING_CONSTANT)]
        shuffle(indices)

        for index in indices:
            if self.hash_table[index]:
                keys = self.hash_table[index]
                shuffle(keys)
                key = keys[0]
                keys.remove(key)
                return key

    def clear(self):
        for index in range(len(self.hash_table)):
            self.hash_table[index] = []


def main():
    my_set = Set()
    my_set.add(4)
    print(my_set.hash_table)
    print(my_set.contains(4))
    my_set.remove(4)
    print(my_set.contains(4))

    my_set.add('one')
    my_set.add('two')
    print(my_set.pop())

    to_add = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for item in to_add:
        my_set.add(item)
    my_set.clear()
    print(my_set.hash_table)


if __name__ == '__main__':
    main()
