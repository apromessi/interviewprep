#!/usr/bin/env python


def linear_search(value, my_list):
    for i, item in enumerate(my_list):
        if item == value:
            return i
    return None


def main():
    my_list = [7, 5, 3, 9, 0, 3, 1, 2, 'b', 'a', 'c']
    print(linear_search(7, my_list))
    print(linear_search(100, my_list))
    print(linear_search(3, my_list))

if __name__ == '__main__':
    main()
