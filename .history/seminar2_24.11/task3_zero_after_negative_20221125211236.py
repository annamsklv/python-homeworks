# 3 - Дан массив размера N. После каждого отрицательного элемента массива 
# вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]
import random

def create_list(num):
    list_of_numbers = []
    for i in range(num):
        list_of_numbers.append(random.randint(-100, 100))
        i += 1
    return(list_of_numbers)

def put_zero_after_negative(list):
    for i in range(len(list)):
        if list[i] < 0:
            list.replace('0')
    return list

        
num = int(input('Введите число:\n'))
print(create_list(num))
print(put_zero_after_negative(create_list(num)))
