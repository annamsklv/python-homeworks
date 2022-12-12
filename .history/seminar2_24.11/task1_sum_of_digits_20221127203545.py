# ; 1 - Напишите программу, которая принимает на вход вещественное число и показывает 
# ; сумму его цифр. Учтите, что числа могут быть отрицательными

# ; Пример:

# ; 67.82 -> 23
# ; (-0.56) -> 11

# num = abs(float(input('Введите вещественное число:\n')))
def is_float(num):  
    try:
        float_input = float(num)
        return float_input
    except ValueError:
        print('это не вещественное число')

def get_int(float_):
    while not float_.is_integer():
        float_ *= 10
    new_int = int(float_)
    return new_int

def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum = sum + (n % 10)
        number = n//10
    return sumdig

    
n = input('Введите вещественное число:\n')
num = abs(is_float(n))
try:
    print(get_int(num))
except AttributeError:
    print('это не число')

print(sum_of_digits(num))




# if num.isdigit():
#     print(num)
# else:
#     print('neint')