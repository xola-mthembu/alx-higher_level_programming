#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists.
    Args:
        my_list_1 (list): First list of numbers.
        my_list_2 (list): Second list of numbers.
        list_length (int): The number of elements to divide.
    Returns:
        A new list with the results of the division.
    """
    new_list = []
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            new_list.append(division)
    return new_list
