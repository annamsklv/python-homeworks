# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x_number = int(input('введите координату x:\n'))
y_number = int(input('введите координату y:\n'))

if x_number == 0:
    print('точка находится на оси ординат')
elif y_number == 0:
    print('точка находится на оси абсцисс')
elif x_number == 0 and y_number == 0:
    print('точка является началом координат')

    
if x_number > 0 and y_number > 0:
    print('1')
elif x_number < 0 and y_number > 0:
    print('2')
elif x_number < 0 and y_number < 0:
    print('3')
el:
    print('4')
