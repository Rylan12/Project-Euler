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


def get_string_repr(array):
    string = ''
    for i in array:
        string += str(i)
    return string


def get_missing_digit(num):
    num = str(num)
    for i in range(10):
        if str(i) not in num:
            return i
    return None


def figure_out_third_digit(a, b, c, mutliple):
    possibilities = []
    values = [a, b, c]
    for i in range(0, 10):
        if a is None:
            values[0] = i
        elif b is None:
            values[1] = i
        elif c is None:
            values[2] = i
        if int(str(values[0]) + str(values[1]) + str(values[2])) % mutliple == 0:
            possibilities.append(i)
    return possibilities


if __name__ == '__main__':
    num = [None, None, None, None, None, None, None, None, None, None]
    final = []
    # 1234567890
    for four in [0, 2, 4, 6, 8]:
        for six in [0, 5]:
            for five in figure_out_third_digit(four, None, six, 5):
                for seven in figure_out_third_digit(five, six, None, 7):
                    for eight in figure_out_third_digit(six, seven, None, 11):
                        for nine in figure_out_third_digit(seven, eight, None, 13):
                            for ten in figure_out_third_digit(eight, nine, None, 17):

                                for three in figure_out_third_digit(None, four, five, 3):
                                    for two in figure_out_third_digit(None, three, four, 2):
                                        num = [None, two, three, four, five, six, seven, eight, nine, ten]
                                        one = get_missing_digit(get_string_repr(num[1:]))
                                        num[0] = one
                                        if is_substring_divisible(get_string_repr(num)):
                                            final.append(int(get_string_repr(num)))
    print(final)
    print(sum(final))

    # d = [
    #     get_multiples(2, 123, 978),
    #     get_multiples(3, 123, 978),
    #     get_multiples(5, 123, 978),
    #     get_multiples(7, 123, 978),
    #     get_multiples(11, 123, 978),
    #     get_multiples(13, 123, 978),
    #     get_multiples(17, 123, 978)
    # ]
    # print(d)

    # nums = []
    # for i in range(1023456789, 9876543211):
    #     if is_substring_divisible(i):
    #         print(i)
    #         nums.append(i)
    # print(nums)
    # print(sum(nums))
