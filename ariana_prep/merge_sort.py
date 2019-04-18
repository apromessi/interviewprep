#!/usr/bin/env python


def merge(list1, list2):
    sorted_list = []

    while list1 and list2:
        if list1[0] <= list2[0]:
            to_add = list1.pop(0)
        else:
            to_add = list2.pop(0)
        sorted_list.append(to_add)

    if list1:
        sorted_list.extend(list1)
    elif list2:
        sorted_list.extend(list2)
    return sorted_list


def merge_sort(my_list):
    if len(my_list) > 1:
        sublist_1 = my_list[:len(my_list)/2]
        sublist_2 = my_list[len(my_list)/2:]
        return merge(merge_sort(sublist_1), merge_sort(sublist_2))
    else:
        return my_list


def main():
    list1 = [7, 5, 3, 9, 0, 1, 2, 100]
    list2 = [0, 5, 3, 9, 0, 1, 0, 100]
    list3 = [0]
    list4 = [100, 90, 8, 7, 4, 3, 0, -5]

    print(merge_sort(list1))
    print(merge_sort(list2))
    print(merge_sort(list3))
    print(merge_sort(list4))


if __name__ == '__main__':
    main()


#############################
# alternatives:

def divide2(my_list):
    if len(my_list) > 1:
        first = my_list[0]
        rest = my_list[1:]
        return [first] + divide2(rest)
    else:
        print(my_list)
        return [my_list]
