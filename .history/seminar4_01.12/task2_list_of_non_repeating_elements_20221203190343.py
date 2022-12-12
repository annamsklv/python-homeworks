# 2 - Задайте последовательность чисел.
#  Напишите программу, которая выведет список неповторяющихся 
#  элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

lst = data = '1 2 3 5 8 15 23 38'.split()

def unique_elements(lst):
    lst_new = []
    for i in range(len(lst)):
        if lst[i] not in lst_new:
            lst_new.append(lst[i])
        else:
            continue
    return lst_new

print(unique_elements(lst))




    