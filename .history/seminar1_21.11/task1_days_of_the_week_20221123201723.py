# ; 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# ; Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон

# ; *Пример:*

# ; - 6 -> да
# ; - 7 -> да
# ; - 1 -> нет

number_of_day = input('Введите цифру, обозначающую день недели:\n')

if number_of_day.isdigit():
    
    num = int(number_of_day)
    if num > 7 or num < 1:
        print('это не цифра, обозначающая день недели')
    elif num > 5:
        print('да')
    else:
        print('нет')
else:
    print('это не цифра, обозначающая день недели')