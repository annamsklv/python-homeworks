# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

input_str = input('Введите текст\n')
trigger_str = input('Введите искомую строку\n')
# print (delete_word(input_str, trigger_str))

lst = [i for i in input_str.split(' ') if not trigger_str in i ]
print(' '.join(lst))


# жди меня и я вернусь жди жди жди -> меня и я вернусь жди (последнее слово не удалилось)