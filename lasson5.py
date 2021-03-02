# # # from datetime import datetime
# # #
# # #
# # # def timeit(func):
# # #     def wrapper():
# # #         start = datetime.now()
# # #         func()
# # #         print(datetime.now() - start)
# # #     return wrapper
# # #
# # # @timeit
# # # def one():
# # #     l = []
# # #     for i in range(10000):
# # #         l.append(i)
# # #     return f"{len(l)}"
# # #
# # # @timeit
# # # def two():
# # #     l = [i for i in range(10000)]
# # #     return f"{len(l)}"
# # #
# # #
# # # first = timeit(one)
# # # second = timeit(two)
# # #
# # #
# # # # one()
# # # #
# # # # two()
# # # print(first())
# # #
# # # def make_upper(func):
# # #     def wrapper():
# # #         return func().upper()
# # #     return wrapper
# # #
# # # def make_lower(func):
# # #     def wrapper():
# # #         return func().lower()
# # #     return wrapper
# # #
# # # @make_upper
# # # def hello():
# # #     return "Hello World"
# # #
# # #
# # # def myfunc():
# # #     return "I like Python"
# # #
# # #
# # # x = make_lower(myfunc)()
# # #
# # # print(x)
# #
# #
# # def decorator_func(func):
# #     def wrapper():
# #         print("Функция обертка")
# #         print(f"Оборачиваемая функция {func}")
# #         print("Выполняеум обернутую фуекцию")
# #         hello()
# #         print("Выходим из обертки")
# #     return wrapper
# #
# # @decorator_func
# # def hello():
# #     print('Hello World')
# #
# #
# #
# #
# # def decorator_func(func):
# #     def wrapper():
# #
# #     return wrapper
# #
# # x = decorator_func(hello)()
# # print(x)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# def one():
#     l = []
#     for i in range(10):
#         l.append(i)
#     return l
#
# list_ = one()
# # print(list_)
#
# def two():
#     l = []
#     for i in range(10):
#         l.append(i)
#     return print(l)
#
# list2 = two()
# print(type(list2))

#
# def burger(func):
#   def bur(*a, **b):
#     print('Верхняя булочка')
#     func(*a, **b)
#     print('Нижняя булочка')
#   return bur
#
# def kotleta(k):
#   def kot(*a, **b):
#     print('курочка')
#     k(*a, **b)
#     print('говядина')
#   return kot
#
# @burger
# @kotleta
#
# def nachinka(cheese, tomatoes, cucumber, sous):
#     print( '\n', cheese,'\n', tomatoes,'\n', cucumber,'\n', sous,'\n',)
#
# nachinka('Сыр','Помидоры','Огурцы', 'Соус')














# # 7. Напишите код для ввода числа. Выведите его 10 цифру по порядку
# # (Учтите, что число может быть коротким, в таком случае начинайте
# # отсчет с первой цифры).
# print('Задание №7')
# number = input('Введите число: ')
# if number.isdigit():
#     if len(number) > 1 and len(number)< 10:
#         number = number * 5
#         print(number)
#         print(int(number[9]))
#     elif len(number) == 1:
#         print(int(number))
#     else:
#         print(int(number[9]))
# else:
#     print('Вы ввели  не число')

# # 8. Напишите программу для сортировки dict по ключам.
# print("Задача №8 ")
# currency = {'Kyrgyzstan': 'som', 'Russia': 'rubli', 'USA': 'dollar', 'UK': 'euro', 'China': 'yuan'}
# currency2 = {}
# cur = sorted(currency.keys())
# print(cur)
# for i in cur:
#     print(i, ':', currency.get(i))


# currency = {'Kyrgyzstan': 'som', 'Russia': 'rubli', 'USA': 'dollar', 'UK': 'euro', 'China': 'yuan'}


# cur2 = list(currency.keys())
# cur2.sort()
#
#
# for key in cur2:
#     print(currency[key])



# # task 17 ---
# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# c = int(input('Введите число: '))
# l = [a, b, c]
# amount = 0
# i = 0
# for i in range(len([a, b, c] )+ 1):
#     if i > 0:
#         amount += 1
#         print(i)
# print(f'Положительных чисел {amount}')

# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
# c = int(input("Третье число: "))
# print('Количество положительных чисел: ', (a > 0) + (b > 0) + (c > 0))


# a, b, c = input("введите числа через пробел: ").split()
# print('Количество положительных чисел: ', (int(a) > 0) + (int(b) > 0) + (int(c) > 0))