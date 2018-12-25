from math import sqrt, ceil


def get_factors(num):
    if num == 1:
        return [1]
    factors = [1]
    if sqrt(num) % 1 == 0:
        factors.append(int(sqrt(num)))
    for i in range(2, ceil(sqrt(num))):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    factors.sort()
    return factors


def is_amicable(num):
    total = sum(get_factors(num))
    other_one = sum(get_factors(total))
    return num == other_one and total != num


if __name__ == '__main__':
    total = 0
    for num in range(2, 10000):
        if is_amicable(num):
            total += num
    print(total)
