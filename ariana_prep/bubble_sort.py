my_list = [7, 5, 3, 9, 0, 1, 2, 100]

my_list = [7, -5, 3, 9, 0, 1, 2, 100]

my_list = [7, 5, 3, 9, 0, 1, 2, None]

my_list = [7, 5, 3, 9, 0, 1, 2, 'a', 'b']

my_list = ['apples', 'cardamom', 'bananas']


def compare_and_swap(my_list):
    swaps = False
    for i in range(len(my_list) - 1):
        item = my_list[i]
        next_item = my_list[i + 1]
        if item > next_item:
            my_list[i] = next_item
            my_list[i + 1] = item
            swaps = True
    return swaps


def bubble_sort(my_list):
    swaps = True
    while swaps:
        swaps = compare_and_swap(my_list)
    return my_list


# note - changes the list in place
