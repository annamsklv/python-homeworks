# 3- Создайте программу для игры в ""Крестики-нолики"".
#  Для определения победы вам может пригодиться функция filter.
# Проверяйте победу после каждого хода, фильтруя столбцы, строки и диагонали по знаку хода
from functions import give_int
area = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['*', '*', '*']
]

def main_menu(area):
    choice = give_int('Выберите знак: нажмите 1, если крестик, 2 - если нолик')
    if choice == 1:
        user = 'x'
    else:
        user = '0'





area[1][1] = 0
print(area)