from solved.p46 import get_primes


def get_distinct_prime_factors(num):
    factors = []
    for prime in get_primes(num):
        if num % prime == 0:
            factors.append(prime)
    return factors


if __name__ == '__main__':
    i = 210
    while True:
        if len(get_distinct_prime_factors(i)) == 4:
            print(i)
            if len(get_distinct_prime_factors(i + 1)) == 4:
                if len(get_distinct_prime_factors(i + 2)) == 4:
                    if len(get_distinct_prime_factors(i + 3)) == 4:
                        print(i, get_distinct_prime_factors(i))
                        print(i + 1, get_distinct_prime_factors(i + 1))
                        print(i + 2, get_distinct_prime_factors(i + 2))
                        print(i + 3, get_distinct_prime_factors(i + 3))
                        break
        i += 1
