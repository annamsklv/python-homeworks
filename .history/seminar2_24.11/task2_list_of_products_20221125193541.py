# 2 - Напишите программу, которая принимает на вход число N и выдает набор 
# произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

num = int(input('a = '))

def factorial(num):
    list_of_products = []
    if num == 1:
        list
        list_of_products.append(list_of_products[i]*list_of_products[i-1]*list_of_products[i-2])