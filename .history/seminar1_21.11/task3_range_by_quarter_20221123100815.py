# 4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# Пример:
# - quarter = 1 = x∈(0, ∞) u y∈(0,∞)

number_of_quarter = int(input('Введите номер четверти:\n'))
quarters =[1, 2, 3, 4]
if number_of_quarter not in quarters:
    print('вы ввели неверное число')
elif number_of_quarter == 1:
    print(x∈(0, ∞) ∪ y∈(0,∞))