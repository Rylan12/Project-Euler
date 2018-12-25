from solved.p022_names import names


def get_alpha_value(name):
    total = 0
    name = name.upper()
    for c in name:
        total += ord(c) - 64
    return total


if __name__ == '__main__':
    names.sort()
    total = 0
    for i in range(len(names)):
        total += (i + 1) * get_alpha_value(names[i])
    print(total)
