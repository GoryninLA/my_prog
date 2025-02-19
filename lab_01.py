# Задание task_01_01.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241
a = int(input("a="))
b = int(input("b="))
print(a + b)
print(a - b)
print(a * b)
print(round(a / b , 2))
print(a // b)
print(a)
print(a * 4)
print(a < b)
print(a != b)
print(a > b)
print(a == b)
print(a <= b)
print(a >= b)

# Задание task_01_02.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


x = int(input("x="))
y = int(input("y="))
z = int(input("z="))
numen = ((((x ** 5) + 7) / (abs(-6) * y))** (1/3)) #числитель
denom = (7 - (z % y)) #знаменатель
result = numen / denom
print(round(result, 3))

# Задание task_01_03.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


# Сопротивление первого проводника
r1 = float(input("r1="))
# # Сопротивление второго проводника
r2 = float(input("r2="))

# # Общее сопротивление
r = r1 + r2
print(round(r, 1)) 

# Задание task_01_04.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


# Двузначное число
num2 = int(input("num2="))
# Трехзначное число
num3 = int(input("num3="))

str_num2 = str(num2)
str_num3 = str(num3)

# 1-я цифра числа 'num2'
num2_1 = int(str_num2[0])
# 2-я цифра числа 'num2'
num2_2 = int(str_num2[1])

# Сумма цифр числа 'num2'
num2_s = num2_1 + num2_2
# Произведение цифр числа 'num2'
num2_p = num2_1 * num2_2

# 1-я цифра числа 'num3'
num3_1 = int(str_num3[0])
# 2-я цифра числа 'num3'
num3_2 = int(str_num3[1])
# 3-я цифра числа 'num3'
num3_3 = int(str_num3[2])

# Сумма цифр числа 'num3'
num3_s = num3_1 + num3_2 + num3_3
# Произведение цифр числа 'num3'
num3_p = num3_1 * num3_2 * num3_3

print(f"Сумма и произведение цифр двузначного числа: {num2_s} {num2_p}")
print(f"Сумма и произведение цифр трехзначного числа: {num3_s} {num3_p}")


# Задание task_01_05.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


# Количество минут
m = 123
# Количество часов, прошедших с начала суток
h = (m // 60)
# Количество минут, прошедших с момента начала последнего часа
m2 = (m - (h * 60))

print(f"Количество минут, прошедшее с начала суток: {m}")
print(f"Количество часов, прошедших с начала суток: {h}")
print(f"Количество минут, прошедших с момента начала последнего часа: {m2}")


# Задание task_01_06.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


a = int(input("Введите a = "))
b = int(input("Введите b = "))
m = int(input("Введите m = "))
n = int(input("Введите n = "))

x = float(-b / a)

is_ok = (m <= x <= n)

print("Попадает:", is_ok)


# Задание task_01_07.
# Выполнил: Горынин.Л.А.
# Группа: ЦИБ-241


team = input("Введите название команды: ")

print(f"{team} - чемпион!")
line = "-" * len(team)
print(line)

# Название команды в нижнем регистре
team_lowercase = team.lower()
print(f"Символов в названии команды: {len(team)}")
print(f'Буква "п" есть: {"п" in team}')
print(f'Количество букв "а": {team.count("а")}')


# Задание task_01_08.
# Выполнил: Горынин.Л.А.
# Группа: ЦИБ-241


# Название государства
country = input("Введите название государства: ")
# Название столицы
capital = input("Введите название столицы: ")
print("Государство - {}, Столица - {}".format(country, capital))


# Задание task_01_09.
# Выполнил: Горынин.Л.А.
# Группа: ЦИБ-241
# E-mail: goryninl@bk.ru


word = "объектно-ориентированный"

w1 = word[:6] 
w2 = word[9:17]
w3 = word[14:17]
w4 = word[4] + word[7] + word[5]
w5 = word[10] + word[12:15] + word[19]
print(w1, w2, w3, w4, w5, sep="\n")


# Задание task_01_10.
# Выполнил: Горынин.Л.А.
# Группа: ЦИБ-241
# E-mail: goryninl@bk.ru

# Создать 2 пустых списка
a = []
b = []

# Добавить 2 вещественных числа (4.5 и 3.4) в список 'a' с помощью append
a.append(4.5)
a.append(3.4)
# Добавить 2 вещественных числа (8.7, 1.3) в список 'a' с помощью extend
a.extend((8.7, 1.3))

# Добавить 2 вещественных числа (14.5, 3.4) в список 'b' с помощью append
b.append(14.5)
b.append(3.4)
# Добавить 2 вещественных числа (8.7, 11.3) в список 'b'с помощью extend
b.extend((8.7, 11.3))


# Вставить целое число 100 на 2-е и 4-е место списка 'a'
a.insert(1, 100)
a.insert(3, 100)

# Вставить целое число 200 на 1-е и 3-е место списка 'b'
b.insert(0, 200)
b.insert(2, 200)

# Вывести списки на экран
print("Исходные списки:")
print(f"1-й: {a}")
print(f"2-й: {b}")

# Удалить первые элементы из списков 'a' и 'b'
del a[0]
del b[0]
# Удалить элемент 100 из списка 'a'
a.remove(100)
# Удалить элемент 200 из списка 'b'
b.remove(200)

# Вывести списки на экран
print("\nПосле удалений:")
print(f"1-й: {a}")
print(f"2-й: {b}")

# Создать множества из списков 'a' и 'b', а также их пересечение
sa = set(a)
sb = set(b)
sa_and_sb = sa.intersection(sb)

# Вывести экран уникальные элементы каждого списка и общие
print("\nУникальные элементы:")
print(f"1-й: {sa}")
print(f"2-й: {sb}")
print("общие:", sa_and_sb)

# Соединить списки 'a' и 'b'
c = a + b 

# Отсортировать список 'c' по возрастанию и убыванию
c_asc = sorted(c)
c_desc = sorted(c, reverse=True)

# # Среднее арифметическое элементов списка 'c', расположенных на четных местах
even_index = c[1::2]
sr_ar = sum(even_index)/len(even_index)
# # Среднее геометрическое элементов списка 'c', расположенных на нечетных местах
odd_index = c[0::2]
start = 1 
for num in odd_index:
    start *= num
sr_geom = round(start ** (1 / len(odd_index)), 2)

# # Максимальный и минимальный элементы
c_max = max(c)
c_min = min(c)
# # Вывести результаты на экран
print("\nИтоговые:")
print("3-й:", c)
print(f"Сортировка (возр.): {c_asc}")
print(f"Сортировка (убыв.): {c_desc}")
print(f"Ср. арифм. = {sr_ar}, Ср. геометр. = {sr_geom}")
print(f"Макс. и мин.: {c_max} {c_min}")


# Задание task_01_11.
# Выполнил: Горынин.Л.А.
# Группа: ЦИБ-241
# E-mail: goryninl@bk.ru

# 1. Создание словаря
info = {}

# Добавить значения для ключей "фио", "дата_рождения", "место_рождения"
info["фио"] = "Горынин Леонид Анатольевич"
info["дата_рождения"] = "14.04.2006"
info["место_рождения"] = "Москва"

# Напечатать словарь
print(info)

# Создать ключ "хобби" со значением = список из строк 
info["хобби"] = ["gaming", "пение", "чтение"]

# Добавить "программирование" в список хобби
info["хобби"].append("программирование")

# Создать ключ "животные" со значением = кортеж из строк 
info["животные"] = ("Кошка Масяня", "Рыбка Гекарим", "Рыбка Дори")


# Создать ключ "ЕГЭ" и поместить в него пустой словарь
info["ЕГЭ"] = {}

# В словарь info["ЕГЭ"] добавить информацию о сданных экзаменах
info["ЕГЭ"]["математика"] = 82
info["ЕГЭ"]["русский"] = 83
info["ЕГЭ"]["литература"] = 100

# # Добавить экзамен, который не был сдан, после чего удалить его
info["ЕГЭ"]["физика"] = 0
del info["ЕГЭ"]["физика"]

# # Создать ключ "вузы" и поместить в него пустой словарь
info["вузы"] = {}

# # В словарь info["вузы"] добавить информацию о вузах,
info["вузы"]["МГУ"] = 296
info["вузы"]["МГПУ"] = 254
info["вузы"]["МГТУ"] = 273

# # 2. Вывод на экран
print("Данные:")
# # Получившийся словарь
print(info)

# # Список экзаменов ЕГЭ в алфавитном порядке
# # (используйте метод ``keys()``, преобразовав результат в кортеж)
exam_key = info["ЕГЭ"]
exams = tuple(sorted(exam_key.keys()))
print("Предметы:", exams)
# # Список вузов в алфавитном порядке
univers_key = info["вузы"]
uni = tuple(sorted(univers_key.keys()))
print("Вузы:", uni)

# # 3. Ответы на вопросы
print("\nОтветы на вопросы:")

# # Выделить имя из info["фио"]
my_name = info["фио"]
name = my_name.split()[1]
# # Начинается на гласную? (True/False)
starts_with_vowel = bool(name[0].lower() in 'аеёиоуыэюя')
print("* мое имя начинается на гласную букву:", starts_with_vowel)

# # Выделить месяц из info["дата_рождения"]
my_month = info["дата_рождения"]
month = my_month.split(".")[1]
# # Родился зимой или летом? (True/False)
born_in_winter_or_summer = month in ["01", "06", "07", "08", "11", "12"]
print("* родился летом или зимой:", born_in_winter_or_summer)

# # Количество хобби и первое из них
my_hobbies = info["хобби"]
hobbies_count = len(my_hobbies)
print("* у меня {} хобби, первое \"{}\"".format(hobbies_count, my_hobbies[0]))

# # Количество сданных экзаменов
print("* после окончания школы сдавал {} экз.".format(len(exam_key)))

# # Сумма баллов по экзаменам
sum_mark = sum(exam_key.values())
print("* сумма баллов = {}".format(sum_mark))

# # Максимальный балл среди сданных
max_mark = max(exam_key.values())
print("* макс. балл = {}".format(max_mark))

# # Количество вузов, в которые Вы проходите по баллам
# # Подсказка: определить, проходите Вы или нет, можно простым сравнением
# # суммы баллов с проходным баллом вуза - ``True/False``.
# # Для того, чтобы определить количество таких вузов, преобразуйте
# # сравнение в целое число (используя ``int()``) и сложите все сравниваемые вузы.
vuz_count = sum(int(sum_mark >= score) for score in univers_key.values())
print("* кол-во вузов в которые прохожу: {}".format(vuz_count))