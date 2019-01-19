from solved.p36 import is_palindrome


def is_lychrel(num):
    for _ in range(50):
        num = num + int(str(num)[::-1])
        # print(num)
        if is_palindrome(num):
            return False
    return True


if __name__ == '__main__':
    count = 0
    for i in range(10000):
        if is_lychrel(i):
            count += 1
    print(count)
