from solved.p24 import factorial

if __name__ == '__main__':
    nums = []
    for i in range(3, 100000):
        total = 0
        for c in str(i):
            total += factorial(int(c))
        if total == i:
            nums.append(i)
            print(i)
    print(sum(nums))
