# 1- Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

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
        list_of_numbers.append(random.randint(0, 10))
    return (list_of_numbers)


def get_sum_of_elements_with_odd_index(lst: list) -> int:
    summ = 0
    for index in range(len(lst)+1):
        if index % 2 != 0:
            summ += lst[index]
    return summ


def get_list_of_elements_with_odd_index(lst: list) -> list:
    lst_of_odd_elements = []
    for index in range(len(lst)+1):
        if index % 2 != 0:
            lst_of_odd_elements.append(lst[index])
    return lst_of_odd_elements


number = give_int('Введите количество элементов списка:\n')
list1 = create_list(number)
print(list1)
print(
    f'на нечётных позициях элементы{get_list_of_elements_with_odd_index(list1)}, их сумма:{get_sum_of_elements_with_odd_index(list1)}')
