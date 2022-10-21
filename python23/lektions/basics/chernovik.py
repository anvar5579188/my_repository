# Напишите функцию, которая
#  будет проходить по диапазону чисел от 1 до 50. 
#  Если число кратно 3 выведите Fizz, в остальных случаях Buzz."""


# def fizzBus():
#     for i in range(1, 51):
#         if i % 3 ==0:
#             print('Fizz')
#     else:
#         print('Buzz')
# fizzBus()

"""Создайте переменную list_ и сохраните в нем список с числами.
 Найдите максимальное число из списка встроенной функцией.
  Результат сохраните в новой переменной result и выведите в консоль."""

# from functools import reduce


# list1 = [1,2,3,4.6,5, 56,-1, -34]

# res = reduce (lambda x,y: x if x>y else y, list1)
# print(res)



#4

# string = 'Anvar'
# print(list(enumerate(string[0:])))



'5'
# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]

# print(list(abs(i) for i in list_))




# list1 =['1', '2', '3', '4', ]
# mapped = map(int, list1)#<map object at 0x7fdcb115bf70>

# print(list(mapped))
'6'
"""В переменной list_ хранится список с разными типами данных, напишите функцию, которая выведет тип данных в последовательности.
Используйте встроенную функцию
Пример:"""
# list_ = ['hello', 123]
# print(list(map(type, list_)))



# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']

# print(list(map(lambda x:x + 'Python' if len(x) >= 5 else x + 'JavaScript', names )))

'8'

# list_ = ['123hello@gmail.com', '123', 'hello']
# print(list(map(lambda x:x if x.endswith('@gmail.com') else 'Not valid email', list_)))




'9'
# list_ = 'hello'
# print(list(enumerate(list_,1)))


# a = {True, 42, 16, 'makers'} 
# a.add('Hello world!')
# print(a)

# from turtle import update




# a =  {1, 2, 3}
# a.discard(5)
# print(a)

# try:

#     for a in  a:
#         a.discard(1)
# except KeyError:
#     print(a)

# a = {1, False, 3}
# a.clear()
# print(a)


'8'

# a = {4, 6, 100, -45, -6} 
# b = {4, 5, -5, -6}

# d = a.intersection(b)
# print(d)

'9'

# a = {2, 4, 6, 50, -45, -6}
# b = {4, 3, 5, -5, -6}

# d = a.difference(b)
# print(d)



a = {0, 1, 2}
b = {0, 1, 2, 3, 34, 5, 8, 13}
if a.issubset(b):
    print('Подмножество! ')
else:
    print()