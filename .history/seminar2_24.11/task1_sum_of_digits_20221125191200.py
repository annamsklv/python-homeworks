# ; 1 - Напишите программу, которая принимает на вход вещественное число и показывает 
# ; сумму его цифр. Учтите, что числа могут быть отрицательными

# ; Пример:

# ; 67.82 -> 23
# ; (-0.56) -> 11

# num = abs(float(input('Введите вещественное число:\n')))
num = str(input('Введите вещественное число:\n'))
def is_int(num):
    try:
        num = int(num)
    except ValueError:
        return False
# print(num)