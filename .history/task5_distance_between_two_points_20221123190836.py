# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21

x_number1 = int(input('введите координату x первой точки:\n'))
y_number1 = int(input('введите координату y первой точки:\n'))
x_number2 = int(input('введите координату x второй точки:\n'))
y_number2 = int(input('введите координату y второй точки:\n'))

distance = round(((x_number2 - x_number1)**2 + (y_number2 - y_number1)**2) ** 0.5, 3) # показывает 3 цифры после запятой
print(distance)
