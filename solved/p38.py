from solved.p32 import is_pandigital

if __name__ == '__main__':
    largest = 0
    for i in range(1000000):
        n = 1
        products = ''
        while len(products) < 9:
            products += str(n * i)
            n += 1
        if is_pandigital(products):
            if int(products) > largest:
                largest = int(products)
    print(largest)
