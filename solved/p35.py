from solved.p27 import is_prime


def is_circular_prime(num):
    num = str(num)
    for i in range(len(num)):
        if not is_prime(int(num)):
            return False
        num = num[1:] + num[0]
    return True


if __name__ == '__main__':
    nums = []
    for i in range(2, 1000000):
        if is_circular_prime(i):
            print(i)
            nums.append(i)
    print(nums)
    print(len(nums))
