def is_pandigital(expr, n=None, zero_based=False):
    expr = str(expr)
    length = len(expr) if n is None else n
    nums = [str(x) for x in range(1 - zero_based, length + 1)]
    for c in expr:
        if c not in nums:
            return False
        nums.remove(c)
    return len(nums) == 0


if __name__ == '__main__':
    products = []
    for i in range(10000):
        for j in range(10000):
            string = str(i) + str(j) + str(i * j)
            if is_pandigital(string, 9):
                print(string)
                products.append(i * j)
    print(list(set(products)))
    print(sum(list(set(products))))
