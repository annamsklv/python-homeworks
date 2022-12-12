# 3- Создайте программу для игры в ""Крестики-нолики"".
#  Для определения победы вам может пригодиться функция filter.
# Проверяйте победу после каждого хода, фильтруя столбцы, строки и диагонали по знаку хода
from typing import List
from functions import give_int


def draw_board(area: List) -> List:
    print('│', area[1], '│', area[2], '│', area[3], '│')
    print('│', area[4], '│', area[5], '│', area[6], '│')
    print('│', area[7], '│', area[8], '│', area[9], '│')

def game(players: List, area: List) -> None:
    pl = players[0]
    for i in range(len(area) - 1):
        new_turn = 10
        while new_turn > 9 or area[new_turn - 1] in ('X', 'O'):
            new_turn = give_int(f'{pl[1]}, куда поставить отметку? Введите число от 1 до 9:', 1)
            if new_turn > 9 or area[new_turn - 1] in ('X', 'O'):
                print('Эта клетка уже занята\n')
        if pl == players[0]:
            area[new_turn] = 'X'
            draw_board(area)
            if i >= 4:
                check_win(area, players[0])
            pl = players[1]
        else:
            area[new_turn] = 'O'
            draw_board(area)
            if i >= 4:
                check_win(area, players[1])
            pl = players[0]


def check_win(area: List, players: List) -> None:
    if area[1] == area[2] == area[3]\
        or area[4] == area[5] == area[6]\
        or area[7] == area[8] == area[9]\
        or area[1] == area[4] == area[7]\
        or area[2] == area[5] == area[8]\
        or area[3] == area[5] == area[8]\
        or area[0] == area[4] == area[8]\
        or area[2] == area[4] == area[6]:
        return exit(print(f'{players[1]} победил!'))
    else:
         return


area = list(range(10))
pl1 = input('Введите имя первого игрока:\n')
pl2 = input('Введите имя второго игрока:\n')
players = [[1, pl1], [2,pl2]]
draw_board(area)
game(players, area)










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