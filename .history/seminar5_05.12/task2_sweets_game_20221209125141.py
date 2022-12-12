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

def turn_maker(player_tuple:List[tuple], number: int = 2021) -> None:
    first_turn = randint(0, 1)
    while number != 0:
        if player_tuple[first_turn][2] == 'man':
            sweet_amount = player_logic(player_name=player_tuple[first_turn][1], num = number)
        elif player
    
