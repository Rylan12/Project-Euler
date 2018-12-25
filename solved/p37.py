from solved.p27 import is_prime


def is_truncatable_prime(num):
    num = str(num)
    for i in range(len(num)):
        if not is_prime(int(num[i:])):
            return False
        if not is_prime(int(num[:len(num) - i])):
            return False
    return True


if __name__ == '__main__':
    nums = []
    for i in range(8, 1000000):
        if is_truncatable_prime(i):
            nums.append(i)
    print(nums)
    print(sum(nums))
