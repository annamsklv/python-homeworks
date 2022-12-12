# 3 - Дан массив размера N. После каждого отрицательного элемента массива 
# вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]
import random

def create_list(num):
    list_of_numbers = []
    for i in range(num):
        list_of_numbers.append(random.randint(-100, 0))
    return(list_of_numbers)

def put_zero_after_negative(list):
    for i in range(len(list)):
        if list[i] < 0:
            if i == - 1: 
                list.append(0)
                list.insert(i+1, 0)  
            else:
                list.append(0) #добавление нуля в случае, если последнее число отрицательное, срабатывает не всегда  
    return list

n = input('Введите число:\n')
if n.isdigit():
    num = int(n)
    new_list = create_list(num)
    print(f'исходный массив:{new_list}')
    try:
        print(f'массив с нулевым значением после каждого отрицательного элемента: {put_zero_after_negative(new_list)}')
    except IndexError:
        print('все числа в массиве положительные')
else:
    print('вы ввели не число')

