#!/usr/bin/env python


def binary_search(my_list, element):
    num_discarded_from_left = 0
    while len(my_list) > 1:
        middle_index = len(my_list) / 2
        sublist_1 = my_list[:middle_index]
        sublist_2 = my_list[middle_index:]
        if element == my_list[middle_index]:
            return middle_index + num_discarded_from_left
        elif element < my_list[middle_index]:
            my_list = sublist_1
        else:
            my_list = sublist_2
            num_discarded_from_left += len(sublist_1)

    if my_list and element == my_list[0]:
        return num_discarded_from_left
    else:
        return None


def binary_search_2(my_list, element):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) / 2
        if element == my_list[mid]:
            return mid
        elif element <= my_list[mid]:
            high = mid - 1
        else:
            low = mid + 1


def main():
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search_2(list1, 0))
    print(binary_search_2(list1, 1))
    print(binary_search_2(list1, 2))
    print(binary_search_2(list1, 7))
    print(binary_search_2(list1, 9))
    print(binary_search_2(list1, 5))
    print(binary_search_2(list1, 11))

    list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search_2(list2, 1))
    print(binary_search_2(list2, 8))
    print(binary_search_2(list2, 10))
    print(binary_search_2(list2, 11))


if __name__ == '__main__':
    main()
