#!/usr/bin/python3

""" Function to determine the minimum number of operations to
result in exactly n H characters of a file
"""


def minOperations(n: int):
    """Calculates the minumum number of operations
    Args:
        n (int): number of H characters in a file
    Returns:
        no_ops (int): number of operations
    """
    if (n < 1):
        return 0

    start = 1
    count = 0
    no_ops = 0

    while start < n:
        rem = n - start
        if (rem % start == 0):
            count = start
            start += count
            no_ops += 2

        else:
            start += count
            no_ops += 1

    return no_ops
