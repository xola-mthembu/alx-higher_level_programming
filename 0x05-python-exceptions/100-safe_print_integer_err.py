#!/usr/bin/python3
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
    except Exception as err:
        import sys
        sys.stderr.write("Exception: {}\n".format(err))
        return False
