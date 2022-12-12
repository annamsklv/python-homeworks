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

from typing import List

# path = ('C:/Users/annam/Desktop/python_homework/seminar4_01.12/Students_and_marks.txt')
# f = open(path, 'r')


def get_list_data(filename: str) -> List[str]:
    '''
    Возвращает список из строк файла
    Args:
    filename - имя файла
    Returns:
    List[str]
    '''
    with open(filename, encoding='utf-8') as file:
        return file.read().split('\n')

# def students_to_caps(lst:list) -> List[str]:
#     trigger_str = '5'
#     for i in range(len(lst)):
#         if trigger_str in lst[i]:
#             lst[i] = lst[i].upper()
#     return lst

def item_to_caps(trigger_str: str, input_str: str) -> str:
    if trigger_str in input_str:
        input_str.upper()
    return input_str
    

# здесь указала путь к файлу, так как при вводе имени файла выходит ошибка "FileNotFoundError: [Errno 2] No such file or directory: 'Students_and_marks.txt'"

lst = get_list_data(
    'C:/Users/annam/Desktop/python_homework/seminar4_01.12/Students_and_marks.txt')

# print (students_to_caps(lst))

