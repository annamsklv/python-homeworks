# ; 1 - Напишите программу, которая принимает на вход вещественное число и показывает 
# ; сумму его цифр. Учтите, что числа могут быть отрицательными

# ; Пример:

# ; 67.82 -> 23
# ; (-0.56) -> 11

# программа работаеттолько с числами до 5 знаков после запятой
# def is_float(num):  
#     try:
#         float_input = float(num)
#         return float_input
#     except ValueError:
#         print('это не вещественное число')

def get_int(float_):
    while round(float_, 5) % 10 != 0:   # трудоности, связанные со спецификой пайтона с округлением чисел, не знаю как преодолеть
        float_ *= 10
    new_int = int(float_)
    return new_int // 10


def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum = sum + (number % 10)
        number = number//10
    return sum

    
n = float(input('Введите вещественное число:\n'))
num = abs(n)
try:
    print(f'{get_int(num)})
    print(sum_of_digits(get_int(num)))

ValueError
AttributeError
TypeError


# def sum_of_digits():
#     number = float(input("Input your number, please: "))
#     sumdig = 0
#     number = abs(number)

#     while round(number, 5) % 10 != 0:
#         number *= 10

#     int(number)

#     while number > 0:
#         digit = number % 10
#         sumdig += digit
#         number = number // 10

#     print(f"The sum of digits in this number is: {int(sumdig)}")

# sum_of_digits()
# # ______________________________________________________________________
# number = list(map(int, input('Введите вещественное число - ').split(',')))
# summ = 0
# for num in number:
#     while num > 0:
#         summ += num%10
#         num = num//10
# print(f'сумма цифр в числе {number[0]},{number[1]} = {summ}')