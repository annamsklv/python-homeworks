# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

from functions import give_int


def is_prime(n):
    div = 2
    lst = []
    for i in range(n):
        if not i % div:
            lst.append(i)
        else: div += 1
    
    return lst if i // div == 1 else print('')

n = give_int('Введите число:\n')
print(n)

print(is_prime(n))

