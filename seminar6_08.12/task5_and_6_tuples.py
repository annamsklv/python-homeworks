# 5 - Есть список случайных чисел в промежутке от 1 до 200, количеством 200.
# Создайте список кортежей, первый элемент которого - индекс элемента,
# а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]
# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

from functions import create_random_list
from typing import List


def check_coincidence(i) -> bool:
    '''
    Проверяет, равен ли один элемент кортежа другому
    arg i - кортеж из двух элементов
    Returns: True/False

    '''
    t1, t2 = i
    if t1 == t2:
        return False
    else:
        return True


def check_multiple_5(i) -> bool:
    '''
    Проверяет, кратна ли сумма элементов кортежа 5
    arg i - кортеж из двух элементов
    Returns: True/False
    '''
    t1, t2 = i
    if (t1 + t2) % 5:
        return False
    else:
        return True


lst = create_random_list(1, 10)
print(lst)

tuples_lst = list(enumerate(lst))
print(tuples_lst)

result1 = list(filter(check_coincidence, tuples_lst))
print(result1)

result2 = list(filter(check_multiple_5, result1))
print(result2)
