from itertools import permutations

from solved.p27 import is_prime


def is_permutation(a, b):
    a, b = str(a), str(b)
    a = [a[i] for i in range(len(a))]
    b = [b[i] for i in range(len(b))]
    a.sort()
    b.sort()
    return a == b


def get_permutations(num):
    num = str(num)
    num = [num[i] for i in range(len(num))]
    return list(permutations(num))


if __name__ == '__main__':
    print(get_permutations(123))
    nums = []
    for n in range(1001,10000, 2):
        if is_prime(n):
            num = get_permutations(n)
            for one in num:
                for two in num:
                    if one != two:



    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10, 2):
                    num = int(str(a) + str(b) + str(c) + str(d))
                    if is_prime(num):
                        primes.append(primes)
