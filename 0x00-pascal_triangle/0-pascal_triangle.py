#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """A function that returns a list of lists of
    integers representing Pascal's triangle of n"""
    if n <= 0:
        return []

    pasTran = []

    for i in range(n):
        # first element
        tempList = [1]
        if i == 0:
            pasTran.append(tempList)
            continue

        k = i - 1
        for j in range(len(pasTran[k])):
            if j + 1 == len(pasTran[k]):
                # last element
                tempList.append(1)
                break
            # Add two previous values to get current next value
            nextVal = pasTran[k][j] + pasTran[k][j + 1]
            tempList.append(nextVal)
        pasTran.append(tempList)

    return pasTran
