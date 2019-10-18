#!/usr/bin/env python


def main(my_list):
    swapped = True
    while swapped is True:
        swapped = False
        for i in range(len(my_list) - 1):
            num = my_list[i]
            next_num = my_list[i + 1]
            if num > next_num:
                my_list[i] = next_num
                my_list[i + 1] = num
                swapped = True

    return my_list



if __name__ == '__main__':
    my_list = [3, 1, 6, 9, 4, 100, 5, 3, 2]

    print main(my_list)