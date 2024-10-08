#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy

    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix

    Returns:
        numpy.ndarray: Result of matrix multiplication

    Raises:
        ValueError: If matrices cannot be multiplied
    """
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
