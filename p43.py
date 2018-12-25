from solved.p32 import is_pandigital


def is_substring_divisible(d):
    d = str(d)
    if not is_pandigital(d, 9, True) or len(d) != 10:
        return False
    if int(d[1] + d[2] + d[3]) % 2 != 0:
        return False
    if int(d[2] + d[3] + d[4]) % 3 != 0:
        return False
    if int(d[3] + d[4] + d[5]) % 5 != 0:
        return False
    if int(d[4] + d[5] + d[6]) % 7 != 0:
        return False
    if int(d[5] + d[6] + d[7]) % 11 != 0:
        return False
    if int(d[6] + d[7] + d[8]) % 13 != 0:
        return False
    if int(d[7] + d[8] + d[9]) % 17 != 0:
        return False
    return True


def get_multiples(num, start, stop):
    multiples = [num]
    i = round(start / num)
    while max(multiples) < stop - stop % num:
        multiples.append(num * i)
        i += 1
    multiples.pop(0)
    return multiples


def get_missing_digit(num):
    num = str(num)
    for i in range(10):
        if str(i) not in num:
            return i
    return None


if __name__ == '__main__':
    d = [
        get_multiples(2, 123, 978),
        get_multiples(3, 123, 978),
        get_multiples(5, 123, 978),
        get_multiples(7, 123, 978),
        get_multiples(11, 123, 978),
        get_multiples(13, 123, 978),
        get_multiples(17, 123, 978)
    ]
    print(d)

    # nums = []
    # for i in range(1023456789, 9876543211):
    #     if is_substring_divisible(i):
    #         print(i)
    #         nums.append(i)
    # print(nums)
    # print(sum(nums))
