# 3- Создайте программу для игры в ""Крестики-нолики"".
#  Для определения победы вам может пригодиться функция filter.
# Проверяйте победу после каждого хода, фильтруя столбцы, строки и диагонали по знаку хода
# from functions import give_int
# coordinates = {1: [0][0], 2: [0][1], 3: [0][2],
#                4: [1][0], 5: [1][1], 6: [1][2],
#                7: [2][0], 8: [2][1], 9: [2][2]
#                }
# # area = [
# #     ['1', '2', '3'],
# #     ['4', '5', '6'],
# #     ['7', '8', '9']
# # ]

# # def main_menu(area):
# #     choice = give_int('Выберите знак: нажмите 1, если крестик, 2 - если нолик\n')
# #     if choice == 1:
# #         user = 'X'
# #     else:
# #         user = '0'

# #     choice2 = give_int(f"['1', '2', '3']\n['4', '5', '6']\n['7', '8', '9']\nКуда поставить {user} ?\n Введите число от 1 до 9\n")
    
# # # area[2][2] = 'x'
# # # print(area)
# # main_menu(area)

# print(coordinates)

board = list(range(1,10))

def draw_board():
    for i in range(3):
        print('│', board[0 + i *3], '│', board[1 + i *3], '│', board[2 + i *3], '│')

def take_input(player_token):
    while True:
        value = input('Куда поставить:' + player_token)
        if not (value in '123456789'):
            print('Ошибочный ввод. Повторите')
            continue
        value = int(value)
        if 





draw_board()