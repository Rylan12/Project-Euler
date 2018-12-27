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
    primes = []
    for i in range(1001, 10000, 2):
        if is_prime(i):
            primes.append(i)
    print(primes)

    for prime in primes:
        if prime == 1487:
            zyx = 123
        perms_tuple = list(permutations(str(prime)))
        perms = []
        for p in perms_tuple:
            num = int(p[0] + p[1] + p[2] + p[3])
            if is_prime(num) and len(str(num)) == 4:
                perms.append(int(p[0] + p[1] + p[2] + p[3]))
        perms = list(set(perms))
        if len(perms) < 3:
            continue
        perms.sort()
        perms.reverse()
        # print(perms)
        for biggest in perms:
            for next_biggest in perms[perms.index(biggest) + 1:]:
                # print(perms[biggest])
                difference = biggest - next_biggest
                if next_biggest - difference in perms:
                    print(biggest, next_biggest, next_biggest - difference)
                    print(str(next_biggest - difference) + str(next_biggest) + str(biggest))
