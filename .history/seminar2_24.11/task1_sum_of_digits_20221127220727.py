# ; 1 - Напишите программу, которая принимает на вход вещественное число и показывает 
# ; сумму его цифр. Учтите, что числа могут быть отрицательными

# ; Пример:

# ; 67.82 -> 23
# ; (-0.56) -> 11


def get_int(float_):
    while round(float_, 5) % 10 != 0:   
        float_ *= 10
    new_int = int(float_)
    return new_int // 10


def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum = sum + (number % 10)
        number = number//10
    return sum

try:    
    n = float(input('введите вещественное число:\n'))
    num = abs(n)
    print(f'число по модулю без запятой:{get_int(num)}')
    print(f'сумма цифр в числе: {sum_of_digits(get_int(num))}')
except ValueError:
    print('вы ввели не число')


# первый тест-кейс не срабатывает из-за специфики округления чисел в python


