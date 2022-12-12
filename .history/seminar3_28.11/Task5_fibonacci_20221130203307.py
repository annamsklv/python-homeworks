# 5-Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


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

def fib(n:int) -> int:
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib_lst(num:int) -> list:


# def fib_positive_list(num:int) -> list:
#     fib_list = [0, 1]
#     for i in range(2, num+1):
#         fib_list.append(fib_list[i-1] + fib_list[i-2])
#     return fib_list

def fib_negative_list(lst:list) -> list:
    lst.reverse()
    for i in range(len(lst)):
        if i % 2 == 0:
            lst[i] *= -1
    return lst
    

n = give_int('Введите число:\n')
positive_list = fib_positive_list(n)
negative_list = fib_negative_list(positive_list)
negative_list.pop(-1)
negative_list.extend(fib_positive_list(n))
print(negative_list)


