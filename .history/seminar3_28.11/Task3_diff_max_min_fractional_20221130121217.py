; 3-Задайте список из вещественных чисел. 
; Напишите программу, которая найдёт разницу между 
; максимальным и минимальным значением дробной части элементов.

; Пример:

; [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
; [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

import random
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


def create_list(num: int, min_num: Optional[int] = None,  max_num: Optional[int] = None) -> list:
    list_of_numbers = []
    for i in range(num):
        list_of_numbers.append(random.randint(0, 15))
    return (list_of_numbers)
