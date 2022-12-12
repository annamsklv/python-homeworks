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

def get_int(float):
    while not float.is_integer():
        float *= 10
    new_int = int(float)
    return new_int

def sum_of_digits(int):
    sum = 0
    while int Ю 0:
        sum += int % 10
    return sum

    
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