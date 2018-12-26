from math import sqrt

from solved.p27 import is_prime


def get_primes(stop):
    primes = []
    for i in range(1, stop):
        if is_prime(i):
            primes.append(i)
    return primes


if __name__ == '__main__':
    i = 9
    while True:
        if is_prime(i):
            # print(i)
            i += 2
            continue
        for prime in get_primes(i):
            if sqrt((i - prime) / 2) % 1 == 0:
                break
        else:
            print(i)
            break
        i += 2
