def is_leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def is_sunday(day):
    return day % 7 == 5


days_in_months = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                  [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

if __name__ == '__main__':
    counter = 0
    day = 0
    for year in range(1901, 2001):
        for month in range(12):
            if is_sunday(day):
                counter += 1
            day += days_in_months[is_leap_year(year)][month]
    print(counter)
