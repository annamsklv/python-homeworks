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


def delete_word(input_str:str, trigger_str:str) -> str:
    lst = input_str.split(' ')
    for i in range(len(lst)):
        if trigger_str in lst[i]:
            lst.pop(i)
    return (' '.join(lst))

trigger_str = 'уб'

print (delete_word(input_str, trigger_str))



