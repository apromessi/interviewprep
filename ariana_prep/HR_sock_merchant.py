#!/usr/bin/env python

# John works at a clothing store. He has a large pile of socks that he must
# pair by color for sale. Given an array of integers representing the color
# of each sock, determine how many pairs of socks with matching colors there are.


def sock_merchant(n, my_list):
    my_list.sort()
    pairs = 0
    while len(my_list) > 1:
        if my_list[0] == my_list[1]:
            pairs += 1
            my_list.pop(0)
        my_list.pop(0)
    return pairs


def main():
    list1 = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]
    list1.sort()
    print(list1)
    print(sock_merchant(20, list1))

if __name__ == '__main__':
    main()
