#!/usr/bin/env python


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        current_item = my_list[i]
        for j in range(i):
            if current_item < my_list[j]:
                my_list.pop(i)
                my_list.insert(j, current_item)
                break
    return my_list


def main():
    list1 = [7, 5, 3, 9, 0, 1, 2, 100]
    list2 = [7, -5, 3, 9, 0, 1, 2, 100]
    list3 = [7, -5, 3, 9, 3, 1, 3, 100]
    list4 = [7, 5, 3, 9, 0, 1, 2, None]
    list5 = [7, 5, 3, 9, 0, 1, 2, 'b', 'a', 'c']
    list6 = ['apples', 'cardamom', 'bananas']

    for my_list in [list1, list2, list3, list4, list5, list6]:
        print('input: {}'.format(my_list))
        insertion_sort(my_list)
        print('output: {}'.format(my_list))

if __name__ == '__main__':
    main()


# how to perform the insertion? python list.insert(index, item)?
# make the list into a linked list?
