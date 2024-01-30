#!/usr/bin/python3
"""Module for lazy matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.
    Args:
        m_a: The first matrix.
        m_b: The second matrix.
    Raises:
        TypeError: If m_a or m_b is not a list of lists of ints/floats.
        ValueError: If m_a or m_b is empty, or if they cannot be multiplied.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("invalid data type for einsum")
    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        raise ValueError("shapes (0,) and (0,) not aligned: "
                         "0 (dim 0) != 0 (dim 0)")
    return np.matmul(m_a, m_b)
