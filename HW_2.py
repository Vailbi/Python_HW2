import random
import math
# Задача 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# inputNum = list(input())
# print(sum(int(x) for x in inputNum if x != '0' and x != ',' and x != '.'))

# Задача 2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# inputNum = int(input())
# result = 1
# total = list()
# for x in range(1, inputNum+1):
#     result *= x
#     total.append(result)
#
# print(total)


# Задача 3
# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input())
#
#
# def func(x):
#     return (1 + 1 / x) ** x
# result = list()
# for i in range(1, n+1):
#     result.append(round(func(i), 2))
#
# print(result)
# print(sum(x for x in result))

# Задача 4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# N = int(input())
#
#
# def creat_arr(x):
#     arr = []
#     for i in range(x):
#         arr.append(random.randint(-x, x))
#     return arr
#
#
# result = creat_arr(N)
#
# f = open('test.txt', 'r')
# print(result)
#
# for i in f.readlines():
#     print(result[int(i)])


# Задача 5
# Реализуйте алгоритм перемешивания списка.

lst = list(range(1, 25, 3))
print(lst)
random.shuffle(lst)
print(lst)
