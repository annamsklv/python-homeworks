# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21
import math

print('Введите, через пробел координаты первой точки: ')
x_number1, y_number1 = map(int, input().split(' '))

print('Введите, через пробел координаты второй точки: ')
x_number2, y_number2 = map(int, input().split(' '))

distance = float(((x_number2 - x_number1)**2 + (y_number2 - y_number1)**2) ** 0.5)  # показывает 3 цифры после запятой
print(roundmath.floor(distance, 3))
