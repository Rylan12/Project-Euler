def fib(num):
    a, b = 0, 1
    index = 0
    while True:
        a, b = b, a + b
        index += 1
        if len(str(a)) >= num:
            return index


if __name__ == '__main__':
    print(fib(1000))
