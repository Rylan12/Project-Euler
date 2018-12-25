if __name__ == '__main__':
    total_sum = 0
    for i in range(2, 194980):
        total = 0
        for d in str(i):
            total += int(d) ** 5
        if total == i:
            total_sum += total
            print(total)
    print(total_sum)
