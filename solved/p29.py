def get_powers(bound):
    powers = []
    for i in range(2, bound + 1):
        for j in range(2, bound + 1):
            powers.append(i ** j)
    powers = list(set(powers))
    powers.sort()
    return powers


if __name__ == '__main__':
    print(len(get_powers(100)))
