# 1- Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
from typing import Optional


def create_list(num):
    list_of_numbers = []
    for i in range(num):
        list_of_numbers.append(random.randint(0, 10))
    return (list_of_numbers)

def give_int(input_string: str, 
            min_nim: Optional[int] = None)