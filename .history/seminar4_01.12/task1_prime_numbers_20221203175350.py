# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

from functions import give_int


def is_prime(n):
    for i in range(2, n):
        if  n % i == 0:
            return True
        else:
            return False


n = give_int('Введите число:\n')
print(n)

print(is_prime(n))

