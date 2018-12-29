from solved.p49 import is_permutation

if __name__ == '__main__':
    num = 1
    while True:
        if is_permutation(num, 2 * num) and is_permutation(num, 3 * num) and is_permutation(num, 4 * num) and is_permutation(num, 5 * num) and is_permutation(num, 6 * num):
            print(num)
            break
        num += 1
