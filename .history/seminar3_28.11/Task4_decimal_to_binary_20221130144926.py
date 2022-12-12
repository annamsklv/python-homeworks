# ; 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# ; Подумайте, как это можно решить с помощью рекурсии.
# ; Не использовать функцию bin

# ; Пример:

# ; 45 -> 101101
# ; 3 -> 11
# ; 2 -> 10
from typing import Optional

def give_int(input_string: str, min_num: Optional[int] = None, max_num: Optional[int] = None) -> int:
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше{min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите больше{max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели не число')

def binary(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else