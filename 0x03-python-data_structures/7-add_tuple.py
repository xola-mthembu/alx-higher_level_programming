#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples, returning a new tuple with the sum of the first and
    second elements of each input tuple.
    """
    a1, a2 = tuple_a + (0, 0)
    b1, b2 = tuple_b + (0, 0)
    return (a1 + b1, a2 + b2)
