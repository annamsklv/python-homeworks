# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

from functions import give_int

lst = [(-3)**i for i in range(give_int('Введите число N:\n'))]
print(lst)
