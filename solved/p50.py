from solved.p27 import is_prime
from solved.p46 import get_primes

if __name__ == '__main__':
    longest = 0
    # isprime = eulerlib.list_primality(999999)
    primes = get_primes(1, 1000000)
    longest_sequence = 0
    for i in range(len(primes)):
        total = primes[i]
        sequence_length = 1
        for j in range(i + 1, len(primes)):
            total += primes[j]
            sequence_length += 1
            if total >= 1000000:
                break
            if is_prime(total) and sequence_length > longest_sequence:
                print(total, sequence_length)
                longest = total
                longest_sequence = sequence_length
    print(longest)

    # for start in get_primes(1, 1000000):
    #     for i in range(1000000, 0, -1):
    #         primes = get_primes(start, i)
    #         if sum(primes) < 1000000 and is_prime(sum(primes)):
    #             print(sum(primes))
    #             break
    #
    # maximum = 0
    # prime = 0
    # for start in range(1000000):
    #     total = 0
    #     i = start
    #     while total < 1000000 - i:
    #         if is_prime(i):
    #             total += i
    #         # if is_prime(total):
    #         #     print(total)
    #         i += 1
    #     if i - start > maximum:
    #         maximum = i - start
    #         print(total, maximum, start, i)
    # print(prime)
