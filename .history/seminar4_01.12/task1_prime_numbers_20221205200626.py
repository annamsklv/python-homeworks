# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]
# теорема вильсона


from functions import give_int


def is_prime(n: int) -> bool:
    '''
    Checks if the given number is prime
    Takes: int number
    Returns: True/False
    '''
    for i in range(2, n):
        if not (n % i):
            return False
    return True


n = abs(give_int('Введите число:\n'))
lst_of_prime_numbers = [i for i in range(2, n+1) if not n % i and is_prime(i)]
print(lst_of_prime_numbers)
