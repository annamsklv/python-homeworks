# 3- Создайте программу для игры в ""Крестики-нолики"".
#  Для определения победы вам может пригодиться функция filter.
# Проверяйте победу после каждого хода, фильтруя столбцы, строки и диагонали по знаку хода

area = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']
]

area[1][1] = 0
print(area)