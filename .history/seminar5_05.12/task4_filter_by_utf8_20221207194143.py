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


def sum_points(lst: list):
        for i in range(len(lst)):
                t1, t2 = lst[i]
                summ = 0
                for char in t2:
                        summ += int(ord(char))
        if summ % t1:
                return False
        else:
                return True


languages_lst = ['python', 'c#', 'Java', 'C++', 'Go',
        'JavaScript', 'PHP', 'Fortran', 'Scratch', 'C']
numbers_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_of_tuples = lambda x,y: list(zip(x,y))
languages_lst_cap = [i.upper() for i in languages_lst]

num_lang_lst = list_of_tuples(numbers_lst, languages_lst_cap)

# print(num_lang_lst)

filter(sum_points, num_lang_lst)


# string = 'C#'
# summ = 0
# for char in string:
#         summ += int(ord(char))
# print(summ)
        