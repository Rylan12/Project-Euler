from math import sqrt

from solved.p46 import get_primes


def get_distinct_prime_factors_ONLY_USE_IN_PROBLEM_47(num):
    factors = []
    for prime in get_primes(1, num):
        if num % prime == 0:
            factors.append(prime)
        if len(factors) > 4:
            return [0, 0, 0, 0, 0]
    return factors


def get_number_of_distinct_prime_factors(num):
    return len(list(set(prime_factors(num))))
    # count = 0
    # while num > 1:
    #     count += 1
    #     # Cycle through numbers that could be factors
    #     for i in range(2, round(sqrt(num) + 1)):
    #         # Divide out all occurrences of i
    #         if num % i == 0:
    #             while True:
    #                 num //= i
    #                 if num % i != 0:
    #                     break
    #             break
    #     else:
    #         break  # num is prime
    # return count


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


if __name__ == '__main__':
    for i in range(1000000):
        if get_number_of_distinct_prime_factors(i) == 4 and get_number_of_distinct_prime_factors(
                i + 1) == 4 and get_number_of_distinct_prime_factors(
                i + 2) == 4 and get_number_of_distinct_prime_factors(i + 3) == 4:
            print(i)
            break

    # on 57000
    # num_factors = 4
    # prime_factors_remembered = [get_distinct_prime_factors_ONLY_USE_IN_PROBLEM_47(i) for i in range(7000, 7003)]
    # i = 7004
    # while True:
    #     prime_factors_remembered.append(get_distinct_prime_factors_ONLY_USE_IN_PROBLEM_47(i))
    #     if len(prime_factors_remembered[0]) == num_factors and len(prime_factors_remembered[1]) == num_factors and len(
    #             prime_factors_remembered[2]) == num_factors and len(prime_factors_remembered[3]) == num_factors:
    #         print(i - num_factors + 1)
    #         break
    #     if i % 1000 == 0:
    #         print(i)
    #     prime_factors_remembered = prime_factors_remembered[1:]
    #     i += 1
