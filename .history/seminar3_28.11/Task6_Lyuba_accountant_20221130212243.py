# ; 6 - Бухгалтер Люба заполняет ведомость по зарплате. У Любы есть два файла - один с фио, другой - с зарплатой за декабрь.

# ; Ей нужно создать третий файл вида "фио, зарплата".
# ; Но Люба совершила ошибку. Она забыла, что в декабре все работники должны получить зарплату по повышенному коэффициенту: 1.5
# ; А еще у босса есть список любимчиков, которым повышенный коэффициэнт будет 2, их фио нужно выделить высоким регистром: 
# ; они получат зарплату раньше.
# ; Создайте сначала словарь на основе первых двух файлов, а дальнейшие действия - с созданным словарем.

# ; Пример:
# ; Файл 1: (разумеется, у вас больше)
# ; Гарри Джеймс Поттер
# ; Дадли Вернон Дурсль

# ; Файл 2:
# ; 10000
# ; 12000

# ; Финальный файл:
# ; Гарри Джеймс Поттер, 15000
# ; ДАДЛИ ВЕРНОН ДУРСЛЬ 24000

# with open('Surname_Name_Patronymic.txt', 'r') as data:
#     data.write('Ivanov Ivan Ivanovich\n')
#     data.write('Petrov Pyotr Petrovich\n')
#     data.write('THE BEST EMPLOYEE EVER\n')
#     data.write("THE BOSS'S NEPHEW\n")
#     data.write("He'll be fired next month\n")

# with open('Salary_list.txt', 'r') as data:
#     data.write('50000\n')
#     data.write('50000\n')
#     data.write('70000\n')
#     data.write('85000\n')
#     data.write('30000\n')

file1 = open(r'C:\Users\annam\Desktop\python_homework\Surname_Name_Patronymic.txt')
print(file1.readline())
file2 = open(r'C:\Users\annam\Desktop\python_homework\Salary_list.txt')
print(file2.readline())

with open('Name_Sala.txt', 'r') as data:
    data.write('50000\n')
    data.write('50000\n')
    data.write('70000\n')
    data.write('85000\n')
    data.write('30000\n')