#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pascal(n):
    previous_row = [1]
    triangle = [previous_row]

    while len(triangle) < n:
        current_row = [1]
        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])
        current_row.append(1)
        triangle.append(current_row)
        previous_row = current_row

    return triangle


# def format_triangle(triangle):
#     n = len(triangle)
#     for i, row in enumerate(triangle):
#         # prepend spaces onto row to form triangle - number of spaces
#         # will be equal to the number of rows minus the 1-indexed row number
#         num_spaces = n - 1 - i
#         for j, num in enumerate(row):
#             num = str(num)
#             row[j] = num
#         print ' ' * num_spaces + ' '.join(row)


def format_triangle(triangle):
    n = len(triangle)
    for i, row in enumerate(triangle):
        # prepend spaces onto row to form triangle - number of spaces
        # will be equal to the number of rows minus the 1-indexed row number
        num_spaces = n - 1 - i
        for j, num in enumerate(row):
            if num % 2 == 0:
                row[j] = ' '
            else:
                row[j] = '●'
        print ' ' * num_spaces + ' '.join(row)


def main():
    triangle = pascal(1)
    format_triangle(triangle)

    print '*****'

    triangle = pascal(4)
    format_triangle(triangle)

    print '*****'

    triangle = pascal(200)
    format_triangle(triangle)


if __name__ == '__main__':
    main()
