#!/usr/bin/python3
"""
Prime Game: More info in the README.md file
"""


def primeNumbers(n):
    """ Get all prime numbers within range
        Args:
            n (int): upper boundary of range. lower boundary is always 1

        Return:
            primeNos (List[int]): list of prime numbers between 1 and n           

    """
    primeNos = []
    filterd = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filterd[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filterd[i] = False
    return primeNos


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNos = primeNumbers(nums[i])
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
