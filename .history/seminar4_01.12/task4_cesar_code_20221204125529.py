# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается 
# на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
#  а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

alphabet = {
    'а':1, 'б':2, 'в':3, 'г':4, 'д':5,'е':6,'ё':7,'ж':8,    
    'з','','','',  '','','','',  '','','','',  '','','','',  '','','','',  

}