# 2 - Задайте последовательность чисел.
#  Напишите программу, которая выведет список неповторяющихся
#  элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

from typing import List

lst = list(input('Введите элементы через пробел:\n').split())


def unique_elements(lst: list) -> list:
    '''
    Creates a new list with with unique elements of an input list
    Takes: list
    Returns:list
    '''
    lst_new = []
    for i in range(len(lst)):
        if lst[i] not in lst_new:
            lst_new.append(lst[i])
        else:
            continue
    return lst_new


try:
    lst_of_numbers = list(map(int, lst))
    print(unique_elements(lst_of_numbers))
except ValueError:
    # это чтобы программа работала не только с числами
    # она и тез приведения к int 
    print(unique_elements(lst))
