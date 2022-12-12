# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

# def delete_word(input_str:str, trigger_str:str) -> str:
#     lst = input_str.split(' ')
#     for word in range(len(lst)):
#         if trigger_str in lst[word]:
#             lst.remove(lst[word])
#             lst.append('')
#         else: word+=1

#     return (' '.join(lst))


input_str = input('Введите текст\n')
trigger_str = input('Введите искомую строку\n')
# print (delete_word(input_str, trigger_str))

lst = [i for i in input_str.split(' ') if not trigger_str in i ]
print(''.joinlst)


# жди меня и я вернусь жди жди жди -> меня и я вернусь жди (последнее слово не удалилось)