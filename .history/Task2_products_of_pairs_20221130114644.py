# 2-Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

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

def get_sum_of_pairs(lst:list)-> int:
    index_1 = 

number = give_int('Введите количество элементов списка:\n')
list1 = create_list(number)
print(list1)