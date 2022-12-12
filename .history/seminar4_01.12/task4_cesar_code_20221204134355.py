# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается 
# на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
#  а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


alphabet = {
    'а':1, 'б':2, 'в':3, 'г':4, 'д':5, 'е':6, 'ё':7, 'ж':8,    
    'з':9, 'и':10, 'й':11, 'к':12, 'л':13, 'м':14, 'н':15, 'о':16, 'п':17, 'р':18, 'с':19,
    'т':20, 'у':21, 'ф':22, 'х':23, 'ц':24, 'ч':25, 'ш':26, 'щ':27, 'ъ':28,
    'ы':29, 'ь':30, 'э':31, 'ю':32, 'я':33
}

word = 'абба'

def numbers(string):
    word_low = string.lower()
    positions = []
    for letter in word_low:
        positions.append(alphabet.get(letter))
    return positions

print(numbers(word))







# choice_side = int(input())
# if choice_side == 1:    #сдвиг вправо
    
# elif choice_side == 2:   #сдвиг влево

# else:          #ошибка
