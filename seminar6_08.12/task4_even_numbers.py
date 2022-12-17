# 4 - Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

from functions import create_random_list


def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum = sum + (number % 10)
        number = number//10
    return sum


lst = create_random_list(10, 100)
print(lst)

result = [i for i in lst if not sum_of_digits(i) % 2]
print(result)
