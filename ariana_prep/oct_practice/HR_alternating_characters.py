# You are given a string containing characters A and B only.
# Your task is to change it into a string such that there are no matching
# adjacent characters. To do this, you are allowed to delete zero or more
# characters in the string.

# Your task is to find the minimum number of required deletions.

def alternatingCharacters(s):
    deletions = 0
    string = [x for x in s]
    i = 0

    while i < len(string) - 1:
        if string[i] == string[i+1]:
            string.pop(i)
            deletions += 1
        else:
            i += 1

    return deletions