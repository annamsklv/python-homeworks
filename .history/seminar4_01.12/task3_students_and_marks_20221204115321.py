#  3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы
#  фамилии тех студентов, которые имеют средний балл более «4».
#  Нужно перезаписать файл.
#  Пример:
#  Ангела Меркель 5
#  Энакин Скайуокер 5
#  Фредди Меркури 3
#  Александр Пушкин 4

#  Программа выдаст:
#  АНГЕЛА МЕРКЕЛЬ 5
#  ЭНАКИН СКАЙУОКЕР 5
#  Фредди Меркури 3
#  Александр Пушкин 4

from functions import get_list_data
from typing import List


def elements_to_caps(lst: list, trigger_str: str) -> List[str]:
    '''
    Changes the case of an item on condition
    Args: 
    lst - list name
    trigger_str - condition    
    Returns: list
    '''
    for i in range(len(lst)):
        if trigger_str in lst[i]:
            lst[i] = lst[i].upper()
    return lst


# здесь указала путь к файлу, так как при вводе имени файла выходит ошибка "FileNotFoundError: [Errno 2] No such file or directory: 'Students_and_marks.txt'"

lst = get_list_data(
    'C:/Users/annam/Desktop/python_homework/seminar4_01.12/Students_and_marks.txt')

print(elements_to_caps(lst, '5'))

with open('C:/Users/annam/Desktop/python_homework/seminar4_01.12/Students_and_marks.txt', 'w') as data:
    for 
    data.write(file1.readline())
    data.write(file2.readline())