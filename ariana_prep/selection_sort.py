#!/usr/bin/env python


def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            current_item = my_list[i]
            if my_list[j] < my_list[i]:
                my_list[i] = my_list[j]
                my_list[j] = current_item
    return my_list


def main():
    list1 = [7, 5, 3, 9, 0, 1, 2, 100]
    list2 = [7, -5, 3, 9, 0, 1, 2, 100]
    list3 = [7, -5, 3, 9, 3, 1, 3, 100]
    list4 = [7, 5, 3, 9, 0, 1, 2, None]
    list5 = [7, 5, 3, 9, 0, 1, 2, 'a', 'b']
    list6 = ['apples', 'cardamom', 'bananas']

    for my_list in [list1, list2, list3, list4, list5, list6]:
        print('input: {}'.format(my_list))
        selection_sort(my_list)
        print('output: {}'.format(my_list))

if __name__ == '__main__':
    main()


# def get_smallest_item(unsorted_list):
#     smallest_item = unsorted_list[0]
#     for i in range(len(unsorted_list) - 1):
#         if unsorted_list[i] < smallest_item:
#             smallest_item = unsorted_list[i]
#     return smallest_item


# def selection_sort(my_list):
#     sorted_list = []
#     unsorted_list = my_list
#     while unsorted_list:
#         smallest_item = get_smallest_item(unsorted_list)
#         sorted_list.append(smallest_item)
#         unsorted_list.remove(smallest_item)
#     return sorted_list
