# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается
# на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо.
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
#  а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


alphabet_a = {
    'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8,
    'з': 9, 'и': 10, 'й': 11, 'к': 12, 'л': 13, 'м': 14, 'н': 15, 'о': 16, 'п': 17, 'р': 18, 'с': 19,
    'т': 20, 'у': 21, 'ф': 22, 'х': 23, 'ц': 24, 'ч': 25, 'ш': 26, 'щ': 27, 'ъ': 28,
    'ы': 29, 'ь': 30, 'э': 31, 'ю': 32, 'я': 33
}

alphabet_b = {
    -32: 'а', -31: 'б', -30: 'в', -29: 'г', -28: 'д', -27: 'е', -26: 'ё', -25: 'ж',
    -24: 'з', -23: 'и', -22: 'й', -21: 'к', -20: 'л', -19: 'м', -18: 'н', -17: 'о', -16: 'п', -15: 'р', -14: 'с',
    -13: 'т', -12: 'у', -11: 'ф', -10: 'х', -9: 'ц', -8: 'ч', -7: 'ш', -6: 'щ', -5: 'ъ',
    -4: 'ы', -3: 'ь', -2: 'э', -1: 'ю', 0: 'я', 1: 'а', 2: 'б', 3: 'в', 4: 'г', 5: 'д', 6: 'е', 7: 'ё', 8: 'ж',
    9: 'з', 10: 'и', 11: 'й', 12: 'к', 13: 'л', 14: 'м', 15: 'н', 16: 'о', 17: 'п', 18: 'р', 19: 'с',
    20: 'т', 21: 'у', 22: 'ф', 23: 'х', 24: 'ц', 25: 'ч', 26: 'ш', 27: 'щ', 28: 'ъ',
    29: 'ы', 30: 'ь', 31: 'э', 32: 'ю', 33: 'я', 34: 'а', 35: 'б', 36: 'в', 37: 'г', 38: 'д', 39: 'е', 40: 'ё', 41: 'ж',
    42: 'з', 43: 'и', 44: 'й', 45: 'к', 46: 'л', 47: 'м', 48: 'н', 49: 'о', 50: 'п', 51: 'р', 52: 'с',
    53: 'т', 54: 'у', 55: 'ф', 56: 'х', 57: 'ц', 58: 'ч', 59: 'ш', 60: 'щ', 61: 'ъ',
    62: 'ы', 63: 'ь', 64: 'э', 65: 'ю', 66: 'я'
}

word = 'абба'
key = -2

def cesar_encrypt(word: str) -> str:
    # выдает список с номерами букв
    positions = [alphabet_a.get(letter) for letter in word.lower()]
    # выдает список с новыми номерами букв
    new_positions = list(map(lambda x: x+key, positions))
    # выдает зашифрованное слово в виде списка
    word_encrypted = [alphabet_b.get(number) for number in new_positions]
    # список в строку
    return(''.join(word_encrypted))


print(cesar_encrypt(word))

def cesar_decrypt(word)


# choice_side = int(input())
# if choice_side == 1:    #сдвиг вправо

# elif choice_side == 2:   #сдвиг влево

# else:          #ошибка
