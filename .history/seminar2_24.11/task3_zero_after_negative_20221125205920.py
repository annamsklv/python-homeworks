# 3 - Дан массив размера N. После каждого отрицательного элемента массива 
# вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]
import random
num = int(input('Введите число:\n'))
list_of_numbers = []
for i in range(num):
    list_of_numbers[i] = random.randint(1, 100)
    i += 1

print(list_of_numbers)
