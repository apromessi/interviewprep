#!/usr/bin/env python

def get_median(num_list):
    num_list.sort()
    if len(num_list) % 2 == 1:
        median = num_list[len(num_list)/2]
    else:
        n1 = num_list[len(num_list)/2]
        n2 = num_list[len(num_list)/2 - 1]
        median = (n1 + n2) / 2.0
    
    return median


def activity_notifications(expenditure, d):
    notices = 0

    for i in range(d, len(expenditure)):
        median = get_median(expenditure[i-d:i])
        if expenditure[i] >= median * 2:
            notices += 1

    return notices


if __name__ == '__main__':
    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    d = 5

    notices = activity_notifications(expenditure, d)
