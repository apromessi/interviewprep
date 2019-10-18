# Alice is taking a cryptography class and finding anagrams to be very useful.
# We consider two strings to be anagrams of each other if the first string's
# letters can be rearranged to form the second string. In other words, both
# strings must contain the same exact letters in the same exact frequency For
# example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

# Alice decides on an encryption scheme involving two large strings where
# encryption is dependent on the minimum number of character deletions required
# to make the two strings anagrams. Can you help her find this number?


def str_to_dict(string):
    new_dict = dict()
    for char in string:
        new_dict[char] = new_dict.get(char, 0) + 1

    return new_dict


def makeAnagram(a, b):
    chars_to_delete = 0

    a_dict = str_to_dict(a)
    b_dict = str_to_dict(b)

    for char in a_dict.keys():
        num_chars_in_a = a_dict[char]
        num_chars_in_b = b_dict.pop(char, 0)
        chars_to_delete += abs(num_chars_in_a - num_chars_in_b)

    for char in b_dict.keys():
        chars_to_delete += b_dict[char]

    return chars_to_delete
