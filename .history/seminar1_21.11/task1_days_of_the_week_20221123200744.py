# ; 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# ; Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон

# ; *Пример:*

# ; - 6 -> да
# ; - 7 -> да
# ; - 1 -> нет

number_of_day = int(input('Введите цифру, обозначающую день недели:\n'))
# if type(number_of_day) == str:
#     print('это не число')
if a.isdigit(number_of_day):

if number_of_day not in range(1,8):
    print('вы ввели неверное число')
elif number_of_day > 5:
    print('да')
else:
    print('нет')
