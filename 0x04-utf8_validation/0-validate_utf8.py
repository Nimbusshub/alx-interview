#!/usr/bin/python3
"""Validate if Data is a valid UTF-8 encoding """


def validUTF8(data):
    """
    Data (List[int]): List of integers
    Returns:
        bool (-> bool): True if valid utf-8 else False

    """
    n_byte = 0

    for i in data:
        if n_byte == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                n_byte = 1
            elif i >> 4 == 0b1110:
                n_byte = 2
            elif i >> 3 == 0b11110:
                n_byte = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            n_byte -= 1
    return n_byte == 0
