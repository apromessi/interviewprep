#!/usr/bin/env python

HASHING_CONSTANT = 717


def hash(key):
    if not (isinstance(key, basestring) or isinstance(key, int)):
        raise Exception('Cannot hash')

    if isinstance(key, basestring):
        ascii_total = 0
        for char in key:
            ascii_total += ord(char)

        key = ascii_total

    index = key % HASHING_CONSTANT
    return index


class HashTable(object):
    def __init__(self):
        self.hash_table = [[] for x in range(HASHING_CONSTANT + 1)]

    def get_key_value_at_index(self, key, index):
        pairs = self.hash_table[index]
        if pairs:
            for key_value in pairs:
                if key == key_value[0]:
                    return (key_value)
        return None

    def insert(self, key, value):
        index = hash(key)
        key_value = self.get_key_value_at_index(key, index)
        if key_value:
            key_value[1] = value
        else:
            self.hash_table[index].append([key, value])

    def lookup(self, key):
        index = hash(key)
        key_value = self.get_key_value_at_index(key, index)

        if key_value:
            return key_value[1]
        else:
            print('Key not found')
            return None

    def remove(self, key):
        index = hash(key)

        key_value = self.get_key_value_at_index(key, index)
        if key_value:
            return self.hash_table[index].remove(key_value)

        print('Key not found. Could not be removed.')
        return None


def main():
    hash_table = HashTable()
    hash_table.insert(1, 'one')
    hash_table.insert(1, 'two')
    hash_table.insert(2, 'three')
    hash_table.insert(718, 'four')
    hash_table.insert('five', 5)
    print(hash_table.hash_table)

    print(hash_table.lookup(1))
    print(hash_table.lookup(3))

    hash_table.remove(1)
    print('**', hash_table.lookup(1))
    hash_table.remove(1)


if __name__ == '__main__':
    main()
