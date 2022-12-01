# Модуль 3. Часть 1.

# Уровень 1

# def main(x, y, p):
#     count = x
#     year_count = 0
#     count_percent = x / 100 * p
#     while count <= y:
#         year_count += 1
#         count += count_percent
#         count = int(count)
#     print(f'Ваш вклад {x} RUB\nВаш процент {p}%\nВаш желаемый вклад {y} RUB\nЧерез {year_count} лет ваш вклад будет {count} RUB')


# main(int(input('Введите ваш вклад ')),int(input('Введите желаемый вклад ')),int(input('Введите ваш процент ')))

# Уровень 2

# def main(n):
#     for i in range(0, n):
#         print('for частный случай цикла while')

# main(int(input('Введите число повторений ')))

# Уровень 3

# def main(n):
#     count = 0
#     for i in str(n):
#         count += int(i)

#     print(count)

# main(int(input('Введите целое число')))

# Модуль 3. Часть 2.

# Уровень 2

# from random import randint

# def main():
#     maxCount = 0
#     n = 5
#     m = [[randint(0, 100) for i in range(n)] for j in range(n)]

#     for i in m:
#         for j in i:
#             if j > maxCount:
#                 maxCount = j

#     print(maxCount)

# main()

# Уровень 3

# def main(d):
#     b = {}
#     keys = list(d.keys())
#     values = list(d.values())

#     for i in range(0, len(values)):
#         b[values[i]] = keys[i]

#     print(b)

# main({"name": "dev", "version": "2", "description": "title"})

# Модуль 3. Часть 3.

# Уровень 1

# from math import sqrt

# def main(a, b, c):
#     p = (a + b + c) / 2
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#     print(s)

# main(3, 4, 5)

# Уровень 2
#

# def main(s):
#     sl = list()
#     for el in s.split():
#         el = el.replace(',', '')
#         el_len = len(el)
#         if (el_len < 5):
#             sl.append(el)
#     print(sl)


# main('''
# lorem ipsum dolor sit amet, consectetur adip leenq, sed do eiusmod tempor incididunt ut labore et, qwkeqkwekqweq
# leoqwi qoowe lqweowqoeo, qwoeowqeoqwoe, qwewqeiiqwewqe, wiqeiwqieqw, qiiqqqq qqq eqweqweqw qwqq kdask, qwk kqwe k kk kqe
# ''')

# Уровень 3

# import itertools

# def max_int(nums):
#     variables = []

#     for l in list(itertools.permutations(nums)):
#         strNum = ""
#         for num in l:
#             strNum += str(num)

#         variables.append(int(strNum))

#     variables.sort()

#     return variables[-1]


# print(max_int([56, 9, 11, 2]))
# print(max_int([3, 81, 5]))

# Модуль 3. Часть 4.

# import json

# def checkUser(login):
#     with open('module3.json', 'r') as f:
#         data = json.load(f)
#         if login in data:
#             return True
#         else:
#             return data

# def login_func(login, password):
#     with open('module3.json', 'r') as f:
#         data = json.load(f)
#         if login in data:
#             if data[login] == password:
#                 print('Данные введены верно')
#         else:
#             print('Данные введены не верно')

# def register(login, password):
#     userInfo = checkUser(login)
#     to_json = {login: password}

#     if userInfo == True:
#         print('Такой юзер уже существует')
#     elif len(userInfo) == 0:
#         print('Юзера не существует, добавляю запись')
#         with open('module3.json', 'w') as f:
#             json.dump(to_json, f)
#     elif len(userInfo) > 0:
#         print('Юзера не существует, добавляю запись')
#         userInfo.update(to_json)
#         with open('module3.json', 'w') as f:
#             json.dump(userInfo, f)


# register('333', '5555')
# login_func('333', '5555')
