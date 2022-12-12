# 3- Создайте программу для игры в ""Крестики-нолики"".
#  Для определения победы вам может пригодиться функция filter.
# Проверяйте победу после каждого хода, фильтруя столбцы, строки и диагонали по знаку хода
from typing import List
from functions import give_int

area = list(range(10))

def draw_board(area: List) -> List:
    print('│', area[1], '│', area[2], '│', area[3], '│')
    print('│', area[4], '│', area[5], '│', area[6], '│')
    print('│', area[7], '│', area[8], '│', area[9], '│')

def game(players: List, area: List) -> None:
    pl = players[0]
    for i in range(len(area) - 1):
        new_turn = 10
        while new_turn > 9 or area[new_turn - 1] in ('XO'):
            new_turn = give_int







pl1 = input('Введите имя первого игрока:\n')
pl2 = input('Введите имя второго игрока:\n')


draw_board(area)










# # print(coordinates)








# board = list(range(1,10))
# wins_coord = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

# def draw_board():
#     for i in range(3):
#         print('│', board[0 + i *3], '│', board[1 + i *3], '│', board[2 + i *3], '│')

# def take_input(player_token):
#     while True:
#         value = input('Куда поставить:' + player_token)
#         if not (value in '123456789'):
#             print('Ошибочный ввод. Повторите')
#             continue
#         value = int(value)
#         if str(board[value - 1] in 'XO'):
#             print('Эта клетка уже занята')
#             continue
#         board[value - 1] = player_token
#         break

# # def check_win():
# #     for each in wins_coord:
# #         if(board[each[0]-1]):







# draw_board()