def get_diagonal_sum(array):
    total = 0
    for i in range(len(array)):
        total += array[i][i]
    for i in range(len(array)):
        total += array[i][len(array) - 1 - i]
    if len(array) % 2 != 0:
        total -= array[len(array) // 2][len(array) // 2]
    return total


def create_spiral_array(size):
    array = [[0 for _ in range(size)] for _ in range(size)]
    row, col = 0, size - 1
    direction = 'left'
    for num in range(size * size, 0, -1):
        array[row][col] = num

        if direction == 'left':
            if in_bounds(row, col - 1, size) and array[row][col - 1] == 0:
                col -= 1
            else:
                direction = 'down'
                row += 1
        elif direction == 'right':
            if in_bounds(row, col + 1, size) and array[row][col + 1] == 0:
                col += 1
            else:
                direction = 'up'
                row -= 1
        elif direction == 'down':
            if in_bounds(row + 1, col, size) and array[row + 1][col] == 0:
                row += 1
            else:
                direction = 'right'
                col += 1
        elif direction == 'up':
            if in_bounds(row - 1, col, size) and array[row - 1][col] == 0:
                row -= 1
            else:
                direction = 'left'
                col -= 1
    return array


def in_bounds(row, col, size):
    return 0 <= row < size and 0 <= col < size


if __name__ == '__main__':
    array = create_spiral_array(1001)
    print(get_diagonal_sum(array))
