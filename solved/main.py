def get_num_paths(row, col, size):
    count = 0
    if row == size and col == size:
        return 1
    elif row == size:
        return count + get_num_paths(row, col + 1, size)
    elif col == size:
        return count + get_num_paths(row + 1, col, size)
    else:
        return count + get_num_paths(row, col + 1, size) + get_num_paths(row + 1, col, size)


if __name__ == '__main__':
    print(get_num_paths(0, 0, 20))
    # 2, 20, 70, 252, 924, 3432, 12870, 48620, 184756,
