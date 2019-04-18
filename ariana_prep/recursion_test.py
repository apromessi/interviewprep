#!/usr/bin/env python


def get_length(my_list):
    if my_list:
        my_list.pop()
        return 1 + get_length(my_list)
    else:
        return 0


def sum_list(my_list):
    if my_list:
        return my_list.pop() + sum_list(my_list)
    else:
        return 0


def fibonacci(index):
    if index > 1:
        return fibonacci(index - 2) + fibonacci(index - 1)
    else:
        return 1


def main():
    list1 = [7, 5, 3, 9, 0, 1, 2, 100]
    print(get_length(list1))
    list1 = [7, 5, 3, 9, 0, 1, 2, 100]
    print(len(list1))

    list2 = [1, 2, 3]
    print(sum_list(list2))

    print(fibonacci(1))
    print(fibonacci(5))

if __name__ == '__main__':
    main()
