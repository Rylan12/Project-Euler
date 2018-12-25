def factorial(num):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product


if __name__ == '__main__':
    index = 1000000 - 1
    n = 10
    items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number_of_items_in_a_group_of_one_number = factorial(n - 1)
    number = ""
    for i in range(n):
        number += str(index // number_of_items_in_a_group_of_one_number)
        index -= int(number[-1]) * number_of_items_in_a_group_of_one_number
        n -= 1
        number_of_items_in_a_group_of_one_number = factorial(n - 1)

    for index in number:
        print(items[int(index)], end='')
        items.pop(int(index))
