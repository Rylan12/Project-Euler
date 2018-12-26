if __name__ == '__main__':
    num = 0
    for i in range(1, 1001):
        num += i ** i
    print(num)
    print(str(num)[-10:])
    # Answer: 9110846701
