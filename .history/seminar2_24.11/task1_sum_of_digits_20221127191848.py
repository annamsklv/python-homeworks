# ; 1 - Напишите программу, которая принимает на вход вещественное число и показывает 
# ; сумму его цифр. Учтите, что числа могут быть отрицательными

# ; Пример:

# ; 67.82 -> 23
# ; (-0.56) -> 11

# num = abs(float(input('Введите вещественное число:\n')))
num = input('Введите вещественное число:\n'))
def is_flo  
    try:
        float_input = float(num)
        return num
    except ValueError:
        print('это не вещественное число')


# if num.isdigit():
#     print(num)
# else:
#     print('neint')