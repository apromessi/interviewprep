#!/usr/bin/env python


def main(my_list):
    for i in range(len(my_list)):
        current = my_list[i]
        for j in range(i):
            if current < my_list[j]:
                my_list.pop(i)
                my_list.insert(j, current)
                break

    return my_list


if __name__ == '__main__':
    my_list = [3, 1, 6, 9, 4, 100, 5, 3, 2]

    print main(my_list)