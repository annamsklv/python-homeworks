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

def get_products_of_pairs(lst:list)-> int:
    product_list = []
    index_1 = 0
    index_2 = -1
    for index_1 in range(len(lst) // 2):
        product_list.append(lst[index_1] * lst[index_2])
        index_1 += 1
        index_2 -= 1
    if len(lst)//2 != 0:
        product_list.append(lst[len(lst)//2] ** 2)
    return product_list


number = give_int('Введите количество элементов списка:\n')
list1 = create_list(number)
print(list1)
print(get_products_of_pairs(list1))