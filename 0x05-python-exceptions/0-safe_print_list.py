#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.
    Returns:
        The number of elements actually printed.
    """
    printed_count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            printed_count += 1
        except IndexError:
            break
    print()
    return printed_count
