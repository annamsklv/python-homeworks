# 2 - Напишите программу, которая принимает на вход число N и выдает набор 
# произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n *factorial(n - 1)


def list_of_products(num):
    product_list = []
    for i in range(1, num+1):
            product_list.append(factorial(i))
    return product_list


n = (input('N = '))
if n.isdigit():
    num = int(n)
    print(list_of_products(num))
else:
    print('Вы ввели не число')



