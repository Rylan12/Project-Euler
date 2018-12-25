from math import sqrt


def get_pentagonal_number(n):
    return int(n * (3 * n - 1) / 2)


def get_pentagonal_sequence(num):
    nums = []
    for n in range(1, num + 1):
        nums.append(get_pentagonal_number(n))
    return nums


def get_difference(j, k):
    return abs(get_pentagonal_number(k) - get_pentagonal_number(j))


def is_pentagonal(num):
    # Pn = n(3n−1)/2
    # 2Pn = 3n^2-n
    # 2Pn + ? = 3(n^2 - 1/3n + ?)
    # 2Pn - 1/12 = 3(n-1/6)^2 - 1/12
    return (1 + sqrt(1 + 24 * num)) / 6 % 1 == 0


if __name__ == '__main__':
    lowest = 100000000000000000
    for j in range(1, 1000000):
        for k in range(1, 1000000):
            if j > k:
                if is_pentagonal(get_pentagonal_number(j)+get_pentagonal_number(k)):
                    if is_pentagonal(get_pentagonal_number(j)-get_pentagonal_number(k)):
                        if get_difference(j, k) < lowest:
                            lowest = get_difference(j, k)
                            print(j, k)
    print(lowest)

    # lowest = 100
    # for j in range(1, 100000000000):
    #     k = j + 1
    #     if j != k and is_pentagonal(get_pentagonal_number(j) + get_pentagonal_number(k)) and is_pentagonal(
    #             get_pentagonal_number(j) - get_pentagonal_number(k)) and get_difference(j, k) < lowest:
    #         lowest = get_difference(j, k)
    #         print(j, k)
    # print(lowest)
