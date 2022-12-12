# ; 1 - Напишите программу, которая принимает на вход вещественное число и показывает 
# ; сумму его цифр. Учтите, что числа могут быть отрицательными

# ; Пример:

# ; 67.82 -> 23
# ; (-0.56) -> 11

# num = abs(float(input('Введите вещественное число:\n')))
def is_float():  
    try:
        float_input = float(num)
        return num
    except ValueError:
        print('это не вещественное число')

def get_int(float):
    while not float.isinteger:
        float *= 10
        new_int = int(float)
        return new_int
    
num = input('Введите вещественное число:\n')




# if num.isdigit():
#     print(num)
# else:
#     print('neint')