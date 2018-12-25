def repeats(num):
    num = str(num)
    num = num.replace('.', '')
    if 'e+' in num:
        num = num[:num.index('e+')]
    for start_index in range(len(num)):
        for length in range(1, len(num) - start_index):
            key = num[start_index:start_index + length]
            situation = "running"
            for index in range(start_index + length, len(num) - length + 1, length):
                check = num[index:index + length]
                if check != key:
                    break
                situation = "ran"
            else:
                if situation == "ran":
                    return key
    return ""


def is_terminating(denominator):
    for k in range(denominator):
        if 10 ** k % denominator == 0:
            return True
    return False


def is_repeating(denominator):
    for k in range(denominator):
        n = get_co_prime_to_10(denominator)
        if n ** k % n == 1:
            return k
    return 0


# I only used these functions
def get_co_prime_to_10(n):
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5
    return n


def get_repeat_length(denominator):
    mod_value = 10 % denominator
    current_mod_value = mod_value
    k = 1
    while True:
        if current_mod_value == 1:
            return k
        current_mod_value = (current_mod_value * mod_value) % denominator
        k += 1


if __name__ == '__main__':
    max_repeat_length = 0
    max_repeat_d = 0
    for d in range(1, 1000):
        d_co_prime = get_co_prime_to_10(d)
        if d_co_prime != 1:
            repeat_length = get_repeat_length(d_co_prime)
            if repeat_length > max_repeat_length:
                max_repeat_length = repeat_length
                max_repeat_d = d
    print(max_repeat_d)
