# https://www.hackerrank.com/challenges/recursive-digit-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

# We define super digit of an integer x using the following rules:

# Given an integer, we need to find the super digit of the integer.

# If  has only 1 digit, then its super digit is .
# Otherwise, the super digit of x is equal to the super digit
# of the sum of the digits of x.

# You are given two numbers n and k. The number p is created by
# concatenating the string n k times.


def get_super_digit(p):
    if len(p) == 1:
        return p
    else:
        num_list = [int(x) for x in p]
        super_digit = sum(num_list)
        return get_super_digit(str(super_digit))


def superDigit(n, k):
    n_result = get_super_digit(n)
    k_result = get_super_digit(str(n_result) * k)
    return k_result