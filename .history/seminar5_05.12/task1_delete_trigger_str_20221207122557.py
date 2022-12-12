# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

def delete_word(input_str:str, trigger_str:str) -> str:
    lst = input_str.split(' ')
    for word in range(len(lst)):
        if trigger_str in lst[word]:
            lst.remove(lst[word])
            lst.append('')
        else: word+=1

    return (' '.join(lst))

trigger_str = 'уб'
input_str = input('Введите ')
print (delete_word(input_str, trigger_str))


