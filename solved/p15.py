def pascals(num):
    if num == 0:
        return [1]
    if num == 1:
        return [1, 1]
    else:
        previous = pascals(num - 1)
        final = [1]
        for i in range(len(previous) - 1):
            final.append(previous[i] + previous[i + 1])
        final.append(1)
        return final


def num_paths(size):
    board = [[0 for _ in range(size + 1)] for _ in range(size + 1)]
    for i in range(size + 1):
        board[i][-1] = 1
        board[-1][i] = 1
    for row in range(size - 1, -1, -1):
        for column in range(size - 1, -1, -1):
            board[row][column] = board[row + 1][column] + board[row][column + 1]
    return board[0][0]


if __name__ == '__main__':
    print(num_paths(2))
