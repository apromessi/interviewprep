#!/usr/bin/env python


def repeatedString(s, n):
    # get number of 'a's in s
    # get number of repetitions of len(s) in n -- n / len(s)
    # get remainder of string and number of 'a's in the remainder

    num_a_in_s = 0
    for char in s:
        if char == 'a':
            num_a_in_s += 1
    repetitions_of_s_in_n = n//len(s)
    a_count = repetitions_of_s_in_n * num_a_in_s
    print(a_count)
    num_leftover = n % len(s)
    print(num_leftover)
    remaining_string = s[:num_leftover]
    for char in remaining_string:
        if char == 'a':
            a_count += 1
    return a_count


def main():
    print(repeatedString('aba', 10))
    print(repeatedString('a', 1000000000000))
    print(repeatedString('gfcaaaecbg', 547602))

if __name__ == '__main__':
    main()
