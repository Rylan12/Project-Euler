from solved.p46 import get_primes


def get_distinct_prime_factors_ONLY_USE_IN_PROBLEM_47(num):
    factors = []
    for prime in get_primes(1, num):
        if num % prime == 0:
            factors.append(prime)
        if len(factors) > 4:
            return [0, 0, 0, 0, 0]
    return factors


if __name__ == '__main__':
    num_factors = 4
    prime_factors_remembered = [get_distinct_prime_factors_ONLY_USE_IN_PROBLEM_47(i) for i in range(7000, 7003)]
    i = 7004
    while True:
        prime_factors_remembered.append(get_distinct_prime_factors_ONLY_USE_IN_PROBLEM_47(i))
        if len(prime_factors_remembered[0]) == num_factors and len(prime_factors_remembered[1]) == num_factors and len(
                prime_factors_remembered[2]) == num_factors and len(prime_factors_remembered[3]) == num_factors:
            print(i - num_factors + 1)
            break
        if i % 1000 == 0:
            print(i)
        prime_factors_remembered = prime_factors_remembered[1:]
        i += 1
