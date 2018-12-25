def cancel(numerator, denominator):
    numerator = str(numerator)
    denominator = str(denominator)
    for num in range(len(numerator)):
        if numerator[num] in denominator:
            return numerator.replace(numerator[num], ''), denominator.replace(numerator[num], '')
    return None


if __name__ == '__main__':
    print(cancel(49, 98))
    print()
    for n in range(10, 100):
        for d in range(10, 100):
            if n == 49 and d == 98:
                zyx = 123
            result = cancel(n, d)
            if result is not None and n % 10 != 0 and d % 10 != 0 and result[1] != '0' and result[0] != '' and result[1] != '' and n != d and n/d < 1 and n / d == int(result[0]) / int(result[1]):
                print(str((n, d)) + ' ' + str(result))
    # 1/4 * 1/5 * 2/5 * 4/8
    print()
    print(1/4 * 1/5 * 2/5 * 4/8)
