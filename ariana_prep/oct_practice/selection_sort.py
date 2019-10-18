#!/usr/bin/env python


def main(my_list):
    for i in range(len(my_list) - 1):
        current = my_list[i]
        index_to_insert = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[index_to_insert]:
                index_to_insert = j

        num_to_insert = my_list[index_to_insert]

        my_list[i] = num_to_insert
        my_list[index_to_insert] = current

    return my_list


if __name__ == '__main__':
    my_list = [3, 1, 6, 9, 4, 100, 5, 3, 2]

    print main(my_list)