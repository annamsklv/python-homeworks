# 3- Создайте программу для игры в ""Крестики-нолики"".
#  Для определения победы вам может пригодиться функция filter.
# Проверяйте победу после каждого хода, фильтруя столбцы, строки и диагонали по знаку хода
from functions import give_int
coordinates = {1: [0][0], 2: [0][1], 3: [0][2],
               4: [0][0], 5: [0][1], 6: [0][2],
               1: [0][0], 2: [0][1], 3: [0][2]
               }
area = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

# def main_menu(area):
#     choice = give_int('Выберите знак: нажмите 1, если крестик, 2 - если нолик')
#     if choice == 1:
#         user = 'x'
#     else:
#         user = '0'


area[0][2] = 'x'
print(area)
