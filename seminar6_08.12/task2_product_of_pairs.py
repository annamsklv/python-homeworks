# 2- Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


from typing import List
from functions import give_int
from functions import create_random_list


def get_products_of_pairs(lst: List[int]) -> List[int]:
    '''
    Возвращает список произведений пар чисел в исходном списке
    '''
    product_lst = [lst[i] * lst[-1 - i]
                   for i in range(len(lst) // 2 + len(lst) % 2)]
    return (product_lst)


list1 = create_random_list(0, 15)
print(list1)
print(get_products_of_pairs(list1))
