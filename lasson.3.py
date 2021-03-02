# # # set_ = {1,2,3,4}
# # # print(type(set_))
# # # set2 = set()
# # # set2 = {1,2,3,4,1,2,3,4}
# # # print(set2)
# # # list_ = [1,2,3,4,5,6,1,2,3,1,2,3]
# # # list_ = set(list_)
# # # print(list_)
# # # set_ = {}
# # # print(type(set_))
# # set_ = {1,7,77,33,867,3,6,9,2,8,0,2,1, 'abc', 'cdr', 'asda'}
# # print(set_)
# #
# # print(len(set_))
# #
# # # add() update() добавляют элементы в множество
# #
# # set_.add(123123)
# # print(set_)
# # set_.add((1,2,3,4))
# # print(set_)
# # set2 = {'a', 'b', 'c', 'd'}
# # set_.update(set2)
# # # set_ = set_ + set2
# # print(set_)
# #
# # # discard() remove() удаление элементов множества
#
# # set_ = {1, 3, 6, 10, 15, 21, 28, 36, 45}
# # set_.discard(10)
# # print(set_)
# # set_.discard(0)
# # # set_.remove(0)
# # set_.clear()
# # print(set_)
# # Метод union() (объединение) возвращает новое множество, содержащее
# # все элементы каждого из множеств.
#
# # set_a = {1, 2, 3, 4}
# # set_b = {4, 5, 6, 7}
# # set_c = set_a.union(set_b)
# # print(set_c)
#
# # Метод intersection() (пересечение) возвращает новое множество,
# # содержащее все элементы, которые есть и в первом множестве, и во
# # втором.
# # set_a = {1, 2, 3, 4}
# # set_b = {4, 5, 6, 7}
# #
# # set_c = set_a.intersection(set_b)
# # print(set_c)
#
# # Метод difference() (разность) возвращает новое множество, содержащее
# # все элементы, которые есть в множестве a_set, но которых нет в
# # множестве b_set.
#
# # set_a = {1, 2, 3, 4, 5, 6, 7}
# # set_b = {4, 5, 6, 7}
# # set_c = set_a.difference(set_b)
# # print(set_a)
# # print(set_c)
# # set_d = set_b.difference(set_a)
# # print(set_d)
#
# # boolean
# # == - сравнение
# # != - не равно
# # < - меньше
# # > - больше
# # <= - меньше или равно
# # >= - больше или равно
# # and
# # or
# # not
# #
# # point = input('Введите вашу оценку: ')
# # if point == '5':
# #     print('Молодец')
# # elif point == '4':
# #     print('хорошо')
# # elif point == '3':
# #     print('Старайся учиться лучше')
# # elif point.isalpha():
# #     print('введите пожалуйста цифру')
# # else:
# #     print('ты можешь лучше!')
#
# point = input('Введите вашу оценку: ')
# if point.isalpha():
#     print('введите пожалуйста цифру')
# elif point.isdigit():
#     if point == '5':
#         print('Молодец')
#     elif point == '4':
#         print('хорошо')
#     elif point == '3':
#         print('Старайся учиться лучше')
#     elif point <= '2':
#         print('ты можешь лучше!')
#     elif point < '0' or point > '5':
#         print('Тут какая то ошибка')
#     else:
#         print('Тут какая то ошибка')

# a = int(input('Input number: '))
# b = int(input('Input number: '))
#
# if a % 10 == 0 or b % 10 == 0:
#     print('Одно из чисел делится на 10 без остатка')
# print(True and True)
# print(True and False)
# print(False and True)
# print(True or False)
# print(False or True)

# text = 'python'
# if text == True:
#     print(True)
# else:
#     print(False)
# if text:
#     print(True)
# list_ = [1,2,3,4,5]
# if 5 in list_:
#     print('5 in list')
# if 10 in list_:
#     print('10 in list')
# else:
#     print('10 not in list')

# text = 'i like python'
# if 'like' in text:
#     print('word "like" in text')
# if 'hello' not in text:
#     print(text)

# range_ = int(input('input range: '))
# for i in range(range_):
#     print(i)
# range(начало, конец, шаг) не включительно "конец"
# break continue

# for i in range(20):
#     print(text)
#     if i == 10:
#         print('break')
#         break
#     print(f'Шаг {i}')

# for i in range(20):
#     print(text)
#     if i == 10:
#         print('continue')
#         continue
#     print(f'Шаг {i}')
import time
from datetime import datetime
# start = datetime.now()
# i = 0
# while i < 1000:
#
#     print('True')
#     # time.sleep(0.4)
#     i = i + 1
#     print(i)
#
# stop = datetime.now()
# print(stop - start)