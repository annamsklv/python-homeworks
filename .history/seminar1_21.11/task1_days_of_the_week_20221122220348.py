# ; 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# ; Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон

# ; *Пример:*

# ; - 6 -> да
# ; - 7 -> да
# ; - 1 -> нет

number_of_day = int(input('Введите цифру, обозначающую день недели:\n'))
if type(n)

week_days = [1, 2, 3, 4, 5, 6, 7]
if number_of_day not in week_days:
    print('вы ввели неверное число')
elif number_of_day == 6 or number_of_day == 7:
    print('да')
else:
    print('нет')
