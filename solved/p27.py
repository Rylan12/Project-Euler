from solved.p21 import get_factors


def is_prime(num):
    if num < 0:
        return False
    if num == 0:
        return True
    if num == 1:
        return False
    return get_factors(num) == [1]


def get_num_primes(a, b):
    n = 0
    result = n ** 2 + a * n + b
    while is_prime(result):
        result = n ** 2 + a * n + b
        n += 1
    return n


def function(a, b, n):
    return n ** 2 + a * n + b


def get_max_n(a, b, function):
    n = 0
    result = function(a, b, n)
    while is_prime(result):
        n += 1
        result = function(a, b, n)
    return n - 1


if __name__ == '__main__':
    num_primes = 0
    ab = (0, 0)
    for a in range(-999, 1000):
        print(a)
        for b in range(-1000, 1001):
            if get_max_n(a, b, function) > num_primes:
                num_primes = get_max_n(a, b, function)
                ab = a, b
    print(ab)
    print(ab[0] * ab[1])
