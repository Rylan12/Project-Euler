coins = [1, 2, 5, 10, 20, 50, 100, 200]


# Didn't use
def get_total(array):
    return (array[0] + 2 * array[1] + 5 * array[2] + 10 * array[3] + 20 * array[4] + 50 * array[5] + 100 * array[
        6] + 200 * array[7]) / 100


def count_possibilities(goal, coin_array):
    # Base case 1: no coins left to use (0 possibilities)
    if goal < 0 or len(coin_array) <= 0:
        return 0
    # Base case 2: goal is zero (1 possibility)
    if goal == 0:
        return 1
    # Recursive call to sum of the 2 possible options
    # One:
    #   Don't use the current coin (recursive call to same goal with coin list minus the last coin)
    # Two:
    #   Use one of the current coin (recursive call to goal minus current coin value with same coin list)
    return count_possibilities(goal, coin_array[:-1]) + count_possibilities(goal - coin_array[-1], coin_array)


if __name__ == '__main__':
    print(count_possibilities(200, coins))
