# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

input_str = (input('Введите текст\n')).lower()
trigger_str = input('Введите искомую строку с маленькой буквы\n')
lst = [i for i in input_str.split(' ') if not trigger_str in i]
print(' '.join(lst))

# Программа работает только с текстом, напечатанным правильно (с пробелами после точек, запятых, тире и т.д.)
