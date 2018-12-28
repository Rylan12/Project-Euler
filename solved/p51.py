from math import sqrt

from solved.p27 import is_prime
from solved.p46 import get_primes


def list_primes(start, stop):
    result = [True for _ in range(stop)]
    result[0], result[1] = False, False
    for i in range(round(sqrt(stop) + 1)):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return [i for (i, is_prime) in enumerate(result) if is_prime and i > start]


def is_eight_prime_value_family(num):
    num = str(num)
    for first in range(len(num)):
        for second in range(first + 1, len(num)):
            total = 0
            for replacement in range(10):
                new_num = num[:first] + str(replacement) + num[first + 1: second] + str(replacement) + num[second + 1:]
                # print(new_num)
                if is_prime(int(new_num)):
                    total += 1
            if total == 8:
                return True
    return False


def is_8_prime_value_number(number, indices):
    # print_the_thing = number == 121313
    prime_count = 0
    not_prime = 0
    number = str(number)
    for i in range(10):
        for j in indices:
            number = number[:j] + str(i) + number[j + 1:]
        if is_prime(int(number)) and number[0] != '0':
            # if print_the_thing:
            #     print(number)
            prime_count += 1
        else:
            not_prime += 1
            if not_prime >= 3:
                return False
    return prime_count == 8


def get_replaceable_digits(number):
    number = str(number)
    digits = [number[i] for i in range(len(number))]
    duplicates = []
    for d in ['0', '1', '2']:
        current = [d, 0, []]
        for i in range(len(digits)):
            if digits[i] == d:
                current[1] += 1
                current[2].append(i)
        if current[1] > 1:
            duplicates.append(current)
    return duplicates


def get_lowest_prime_with_pattern(num, indices_to_ignore):
    num = str(num)
    indices_to_save = []
    for i in range(len(num)):
        if i not in indices_to_ignore:
            indices_to_save.append(i)
    primes = list_primes(10 ** (len(num) - 1), 10 ** len(num))
    for prime in primes:
        prime = str(prime)
        for i in indices_to_save:
            if prime[i] != num[i]:
                break
        else:
            return prime
    return False


if __name__ == '__main__':
    # Length of number
    for n in range(4, 10):
        # List of primes of give length
        primes = list_primes(10 ** (n - 1), 10 ** n)
        # print(primes)
        for prime in primes:
            replaceable = get_replaceable_digits(prime)
            for i in replaceable:
                if is_8_prime_value_number(prime, i[2]):
                    print(prime)
                    # print(get_lowest_prime_with_pattern(prime, i[2]))
                    quit(0)

    # Stopped at 5310001
    # primes = get_primes(100, 10000000)
    # print(primes)
    # for i in range(200001, 10000000, 2):
    #     if is_prime(i):
    #         if is_eight_prime_value_family(i):
    #             print(i)
    #             break
    #     if i % 1000 == 1:
    #         print(i)
