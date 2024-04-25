#!/usr/bin/python3
"""
This module provides a function to find a peak element in a list of
unsorted integers. A peak is defined as an element that is not smaller
than its neighbors. The function uses a modified binary search to
achieve efficient searching.
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Arguments:
    list_of_integers -- A list of integers where a peak element is to be found.

    Returns:
    An integer representing a peak, or None if the list is empty or no peak
    is found.
    """
    if not list_of_integers:
        return None
    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]


if __name__ == "__main__":
    # Example use of the find_peak function
    sample_list = [1, 2, 4, 6, 3]
    peak = find_peak(sample_list)
    print(f"Peak found: {peak}")
