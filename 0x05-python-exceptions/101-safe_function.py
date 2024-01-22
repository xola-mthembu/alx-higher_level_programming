#!/usr/bin/python3
def safe_function(fct, *args):
    """
    Executes a function safely.
    Args:
        fct: A pointer to a function.
        args: Arguments to be passed to the function.
    Returns:
        The result of the function or None if an exception occurs.
    """
    try:
        return fct(*args)
    except Exception as err:
        import sys
        sys.stderr.write("Exception: {}\n".format(err))
        return None
