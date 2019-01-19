def sum_power(a, b):
    num = a ** b
    total = 0
    for c in str(num):
        total += int(c)
    return total


if __name__ == '__main__':
    maximum = 0
    for a in range(100):
        for b in range(100):
            s = sum_power(a, b)
            if s > maximum:
                maximum = s
    print(maximum)
