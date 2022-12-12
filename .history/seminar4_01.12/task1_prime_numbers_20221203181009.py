# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

from functions import give_int


def is_prime(n):
    for i in range(2, n):
        if not (n % i):
            return False
    return True

def give_lst(n):
    lst = []
    for i in range(n):
        if n // i == 0 and :




n = abs(give_int('Введите число:\n'))



