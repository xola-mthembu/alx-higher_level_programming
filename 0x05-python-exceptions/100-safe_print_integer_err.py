#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """
    Prints a value as an integer if possible.
    Args:
        value: The value to be printed.
    Returns:
        True if the value was printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
