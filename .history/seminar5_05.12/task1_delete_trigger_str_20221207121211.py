# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

input_str = '''
Я сразу смазал карту будня,
плеснувши краску из стакана;
я показал на блюде студня
косые скулы океана.
На чешуе жестяной рыбы
прочел я зовы новых губ.
А вы
ноктюрн сыграть
могли бы
на флейте водосточных труб?'
'''


# def delete_word(input_str:str, trigger_str:str) -> str:
#     lst = input_str.split(' ')
#     for word in range(len(lst)):
#         try:
#             if trigger_str in lst[word]:
#                 lst = lst.remove(lst[word])
#         except IndexError: word+=1

#     return (' '.join(lst))

# trigger_str = 'уб'

# print (delete_word(input_str, trigger_str))

lst = input_str.split(' ')
print(lst[1])

