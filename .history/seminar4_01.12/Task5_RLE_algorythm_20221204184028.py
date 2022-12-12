# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#  Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol

str = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'

for i in range(len(str)-1):
    if str[i] == str[i+1]:
        count = str.count(str[i])
       
        # res_str = input_string.replace(input_string[i], '')
        res_str = str[:i+1] + str[count-1:]
        print

# res_str = str[:1] + str[12:]
# print(res_str)


      
