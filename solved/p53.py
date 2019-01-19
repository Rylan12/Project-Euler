from math import factorial


def combinations(n, r):
    """
    Returns the number of combinations of n options when selection r items (nCr)
    :param n: Number of options
    :param r: Number selected
    :return: Number of possible ways to select r items from n options
    """
    return int(factorial(n) / (factorial(r) * factorial(n - r)))


if __name__ == '__main__':
    num = 0
    for n in range(1, 101):
        for r in range(1, n):
            if combinations(n, r) > 1000000:
                num += 1
    print(num)
