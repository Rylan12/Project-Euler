from solved.p21 import get_factors


def is_abundant(num):
    if num == 0:
        return False
    return sum(get_factors(num)) > num


def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # these two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x
    return None


if __name__ == '__main__':
    abundant_numbers = []
    for i in range(12, 28123):
        if is_abundant(i):
            abundant_numbers.append(i)
    abundant_numbers.sort()
    print("Found all abundant numbers")
    print(abundant_numbers)

    solution_nums = []
    for target in range(28123, 0, -1):
        if target == 24:
            zyx = 123
        for abundant_num in abundant_numbers:
            if binary_search(abundant_numbers, target - abundant_num) is not None:
                break
        else:
            solution_nums.append(target)
    print(solution_nums)
    print(sum(solution_nums))

    # sums = []
    #
    # while len(abundant_numbers) > 0:
    #     abundant_numbers_2 = abundant_numbers.copy()
    #     while len(abundant_numbers_2) > 0:
    #         sums.append(abundant_numbers[0] + abundant_numbers_2[0])
    #         abundant_numbers_2.pop(0)
    #     abundant_numbers.pop(0)
    # print("Found all sums")
    #
    # total = 0
    # for i in range(28124, 1, -1):
    #     if sums[-1] != i:
    #         total += i
    #     else:
    #         sums.pop(-1)
    #         # sums = sums[1:]
    #
    # print(total)
    # abundants = []
    # for i in range(12, 28123):
    #     if is_abundant(i):
    #         abundants.append(i)
    # print("Calculated abundant numbers. There are: %d" % len(abundants))
    #
    # total = 0
    # for num in range(1, 28123):
    #     if num == 24:
    #         abc = 123
    #     situation = ""
    #     i = 0
    #     while abundants[i] + abundants[0] <= num:
    #         j = 0
    #         while abundants[i] + abundants[j] <= num:
    #             if abundants[i] + abundants[j] == num:
    #                 situation = "totally done"
    #                 break
    #             j += 1
    #         if situation == "totally done":
    #             break
    #         i += 1
    #     if situation != "totally done":
    #         total += num
    #
    # print(total)
