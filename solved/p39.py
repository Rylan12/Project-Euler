from math import sqrt


def get_possible_side_length(perimeter):
    solutions = []
    for a in range(1, int(perimeter / 2) + 1):
        for b in range(1, int(perimeter / 2) + 1):
            c = sqrt(a * a + b * b)
            if a + b + c == perimeter:
                solutions.append([a, b, int(c)])
    return solutions[:int(len(solutions) / 2)]


if __name__ == '__main__':
    maximum = (0, 0)
    for i in range(1001):
        if len(get_possible_side_length(i)) > maximum[1]:
            maximum = (i, len(get_possible_side_length(i)))
    print(maximum)
