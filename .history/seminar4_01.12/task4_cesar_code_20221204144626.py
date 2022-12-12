# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается 
# на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
#  а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


encrypt_alphabet = {
    'а':1, 'б':2, 'в':3, 'г':4, 'д':5, 'е':6, 'ё':7, 'ж':8,    
    'з':9, 'и':10, 'й':11, 'к':12, 'л':13, 'м':14, 'н':15, 'о':16, 'п':17, 'р':18, 'с':19,
    'т':20, 'у':21, 'ф':22, 'х':23, 'ц':24, 'ч':25, 'ш':26, 'щ':27, 'ъ':28,
    'ы':29, 'ь':30, 'э':31, 'ю':32, 'я':33
}

decrypt_alphabet = {


    1:'а', 2:'б', 3:'в', 4:'г', 5:'д', 6:'е', 7:'ё', 8:'ж',    
    9:'з', 10:'и', 11:'й', 12:'к', 13:'л', 14:'м', 15:'н', 16:'о', 17:'п', 18:'р', 19:'с',
    20:'т', 21:'у', 22:'ф', 23:'х', 24:'ц', 25:'ч', 26:'ш', 27:'щ', 28:'ъ',
    29:'ы', 30:'ь', 31:'э', 32:'ю', 33:'я', 34
}

word = 'ьэюя'
shift = -2

positions = [encrypt_alphabet.get(letter) for letter in word.lower()] # выдает список с номерами букв


# new_positions = list(map(lambda x:x+shift,positions))  # выдает список с новыми номерами букв
# translated = [decrypt_alphabet.get(number) for number in new_positions] # выдает зашифрованное слово в виде списка
# print(''.join(translated))



# choice_side = int(input())
# if choice_side == 1:    #сдвиг вправо
    
# elif choice_side == 2:   #сдвиг влево

# else:          #ошибка
