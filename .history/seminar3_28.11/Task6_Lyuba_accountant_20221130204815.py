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

with open('Surname_Name_Patronymic', 'a') as data:
    data