# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#   Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
#   чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from functions import give_int
from typing import List
from random import randint


def player_logic(player_name: str, turn_limitation: int = 28, num: int = 2021) -> int:

    sweet = 0
    while not 0 < sweet <= turn_limitation:
        sweet = give_int(f'{player_name}, сколько конфет вы хотите взять?\n', 1)
        if sweet > turn_limitation:
            print(f'Вы не можете взять больше, чем{turn_limitation}')
        elif sweet > num:
            print(f'Вы не можете взять больше, чем{num}')

    return sweet

def bot_logic(player_name:str, turn_limitation: int = 28, num: int = 2021) -> int:
    sweet = 0
    if player_name == 'Hard Bot':
        if num <= turn_limitation:
            sweet = num
        else:
            if num % turn_limitation > 1:
                sweet = turn_limitation -1
            else:
                sweet = turn_limitation - turn_limitation + 1
    elif player_name == 'Easy Bot':
        if num <= turn_limitation:
            sweet = num
        else:
            sweet = randint(1, 28)
    print(f'{player_name} берет {sweets} конфет')
    






# def turn_maker(player_tuple:List[tuple], number: int = 2021) -> None:
#     first_turn = randint(0, 1)
#     while number != 0:
#         if player_tuple[first_turn][2] == 'man':
#             sweet_amount = player_logic(player_name=player_logic[first_turn][1], num = number)
#         elif player_tuple[first_turn][2] == 'bot':
#             sweet_amount = player_logic(player_name=bot_logic[first_turn][1], num = number)

    
