#!/usr/bin/python3
# 12-pascal_triangle.py
# Alsabti ghaida
"""Module that defines Pascal's Triangle."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): Number of rows.

    Returns:
        list: A list of lists representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle