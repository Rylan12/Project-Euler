from solved.p042_words import words


def get_letter_value(letter):
    alpha = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    if letter in alpha[0]:
        return alpha[0].index(letter) + 1
    if letter in alpha[1]:
        return alpha[1].index(letter) + 1
    return 0


def get_word_value(word):
    total = 0
    for c in word:
        total += get_letter_value(c)
    return total


def get_triangle_limit(stop):
    triangles = []
    for i in range(1, stop + 1):
        triangles.append(int(0.5 * i * (i + 1)))
    return triangles


# 27
if __name__ == '__main__':
    triangle_words = []
    triangle_number = get_triangle_limit(30)
    for word in words:
        if get_word_value(word) in triangle_number:
            triangle_words.append(word)
    print(triangle_words)
    print(len(triangle_words))
