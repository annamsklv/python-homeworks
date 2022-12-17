from typing import Optional
from typing import List
from random import randint

def give_int(input_string: str, min_num: Optional[int] = None, max_num: Optional[int] = None) -> int:
    '''
    Takes an int number from user
    Takes: string
    Returns: int number or a message about an error
    '''
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше{min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите больше{max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели не число')



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

def create_random_list(min:int, max:int) -> List:
    '''
    Возвращает список из случайных чисел с количеством элементов, запрашиваемым у пользователя
    arg num - количество элементов списка
    min, max - границы случайного числа
    returns: List
    '''
    num = give_int('Введите количество элементов списка:\n')
    list_of_numbers = [randint(min, max) for i in range(num)]
    return (list_of_numbers)