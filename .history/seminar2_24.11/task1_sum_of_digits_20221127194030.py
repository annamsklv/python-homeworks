# ; 1 - Напишите программу, которая принимает на вход вещественное число и показывает 
# ; сумму его цифр. Учтите, что числа могут быть отрицательными

# ; Пример:

# ; 67.82 -> 23
# ; (-0.56) -> 11

# num = abs(float(input('Введите вещественное число:\n')))
def is_float(num):  
    try:
        float_input = float(num)
        return float(num)
    except ValueError:
        print('это не вещественное число')

def get_int(num):
    while not num.is_integer:
        num *= 10
        new_int = int(num)
        return new_int
    
n = input('Введите вещественное число:\n')
num = is_float(n)
print(get_int(num))



# if num.isdigit():
#     print(num)
# else:
#     print('neint')