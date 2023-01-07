#!/usr/bin/python3
"""A method that determines if all locked boxes can be opened"""


def canUnlockAll(boxes):
    """Lockbox funtion
    Args:
        boxes: list of list (int)

    Returns: (boolean) if an boxes can be opened or not
    """
    unlockedBox = set()

    for boxId, box in enumerate(boxes):
        if len(box) == 0 or boxId == 0:
            unlockedBox.add(0)
        for key in box:
            if key < len(boxes) and key != boxId:
                unlockedBox.add(key)
    if len(unlockedBox) == len(boxes):
        return True
    return False
