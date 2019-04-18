#!/usr/bin/env python


def maximize_profits(prices):
    max_profit = 0
    lowest = prices[0]
    highest = prices[0]
    for price in prices:
        if price > highest and max_profit < price - lowest:
            highest = price
            max_profit = highest - lowest
        if price < lowest:
            lowest = price
            highest = price
    return max_profit


def main():
    list1 = [7, 3, 5, 2, 6, 5]  # 4
    list2 = [2, 5, 1, 3, 6, 2]  # 5
    list3 = [9, 8, 7, 5, 3, 1]  # 0

    print(maximize_profits(list1))
    print(maximize_profits(list2))
    print(maximize_profits(list3))

if __name__ == '__main__':
    main()
