# 4-Создайте два списка — один с названиями языков программирования, другой — с их нумерацией.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая (обязательно используйте tuple unpacking) — которая отфильтрует этот список следующим образом:
# если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается,
# его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&
from typing import List

languages_lst = ['python', 'c#', 'Java', 'C++', 'Go',
                 'JavaScript', 'PHP', 'Fortran', 'Scratch', 'C']
numbers_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sum_points(lst: list) -> List:
        '''
        '''
        new_lst = []
        sum_lst = []
        for i in lst:
                t1, t2 = i
                summ = 0
                for char in t2:
                        summ += ord(char)
                if not summ % t1:
            new_lst.append(t2)
            sum_lst.append(summ)
return (f'Преобразованный список: {list(zip(sum_lst, new_lst))},\nСумма чисел:{sum(sum_lst)}')


def list_of_tuples(x, y): return list(zip(x, y))


languages_lst_cap = [i.upper() for i in languages_lst]

num_lang_lst = list_of_tuples(numbers_lst, languages_lst_cap)

print(f'Список кортежей: {num_lang_lst}')
print(sum_points(num_lang_lst))
