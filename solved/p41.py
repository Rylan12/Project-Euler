from solved.p27 import is_prime
from solved.p32 import is_pandigital

if __name__ == '__main__':
    nums = []
    for i in range(7654321, 0, -1):
        # 2765143
        if is_prime(i) and is_pandigital(str(i)):
            print(i)
            nums.append(i)
    print(nums)
    print(max(nums))
