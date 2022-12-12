# ; 1 - Напишите программу, которая принимает на вход вещественное число и показывает 
# ; сумму его цифр. Учтите, что числа могут быть отрицательными

# ; Пример:

# ; 67.82 -> 23
# ; (-0.56) -> 11


# # def is_float(num):  
# #     try:
# #         float_input = float(num)
# #         return float_input
# #     except ValueError:
# #         print('это не вещественное число')

def get_int(float_):
    while float_ % 10 != 0:
        float_ *= 10
        print(float_)
    new_int = int(float_)
    return new_int

num = float(input('введите число:\n'))
print(get_int(num))





# # def sum_of_digits(number):
# #     sum = 0
# #     while number > 0:
# #         sum = sum + (number % 10)
# #         number = number//10
# #     return sum

    
# # n = input('Введите вещественное число:\n')
# # num = abs(is_float(n))
# # try:
# #     print(get_int(num))
# # except AttributeError:
# #     print('это не число')

# # print(sum_of_digits(get_int(num)))




# def sum_of_digits():
#     number = float(input("Input your number, please: "))
#     sumdig = 0
#     number = abs(number)

#     while number % 10 != 0:
#         number *= 10

#     int(number)

#     while number > 0:
#         digit = number % 10
#         sumdig += digit
#         number = number // 10

#     print(f"The sum of digits in this number is: {int(sumdig)}")

# sum_of_digits()