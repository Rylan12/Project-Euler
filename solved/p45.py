from math import sqrt

from solved.p42 import get_triangle_limit
from solved.p44 import is_pentagonal


def is_hexagonal(num):
    return (1 + sqrt(1 + 8 * num)) / 4 % 1 == 0


if __name__ == '__main__':
    for t in get_triangle_limit(40755, 100000):
        if is_pentagonal(t) and is_hexagonal(t):
            print(t)
            break
