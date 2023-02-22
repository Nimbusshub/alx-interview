#!/usr/bin/python3
""" A function that determines the fewest number of coins
neededto meet a given amount total
"""


def makeChange(coins, total):
    """Determines the fewest number of coins
    Args:
        coins (list[int]) : list of values of changes
        total (int): The given amount

    Return:
        change (int): the fewest number of coin
    """

    if total < 1:
        return 0
