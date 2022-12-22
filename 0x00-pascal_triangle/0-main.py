#!/usr/bin/python3
"""script to test pascal's triangle function"""

pascal_triangle = __import__('0-pascal_triangle').pascal_triangle


def print_triangle(triangle):
    """Prints the triangle"""
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(6))
    print()
    print()

    print_triangle(pascal_triangle(15))

    print_triangle(pascal_triangle(0))

    print()
    print()

    print_triangle(pascal_triangle(1))
