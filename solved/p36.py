def get_base_two(num):
    return str(bin(num))[2:]


def is_palindrome(num):
    num = str(num)
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            return False
    return True


if __name__ == '__main__':
    nums = []
    for i in range(1000000):
        if is_palindrome(i) and is_palindrome(get_base_two(i)):
            nums.append(i)
    print(sum(nums))
