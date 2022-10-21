'=========================Dekoratory========================='

# dekoratiry - eto funkcii vyshego poryadke - eto funkcia kotorya kotoraya prinimaet argumenty funkci, sozdaet vnutri sebya
#funkcii , vyzyvaet funkcii i vozvroshaet a
#funkcii 
# dekorator = funkciya vyshego poryadka, kotoraya nugna ctoby radhiryat funkcional
# funkcii ne izmenya ee (funkcii obetka )


# from curses.ascii import isupper
# from datetime import datetime


# def decorator(func):
#     def wapper(*args, **kwargs):
#         from datetime import time 
#         print('start:', datetime.now())
#         func(*args, **kwargs)
#         print('finish:', datetime.now())
#     return wapper

# def hello():
#     print('Hello world')

# decorator(hello)()


# 'Sintaksicheski sahar'

# @decorator
# def hello():
#     print('Hello world')

# hello()
# #@ decorator -> hello == decorator

# @decorator
# def mysqrt(x):
#     print(x**0.5)
# mysqrt(25)


# def func_start_time(func):
#     def wrapper(*a, **k):
#         from datetime import date
#         now = datetime.now()
#         correct_format = now.strftime('%H.%M.%S')
#         print('Функция запущена', correct_format)
#         func(*a, **k)
#     return wrapper

# @func_start_time
# def func():
#     print('Hello world')
# func()





# string = 'python is the best'
# if string.startswith('python'):
#     print(True)
# else:
#     print(False)

# string = 'python is the best'
# if string.isupper.startswith('python'):
#     print(True)
# else:
#     print(False)

# string = 'Hello World'
# string1 = list(string)
# print(string.split())


# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {}

# for k in list_:
#     v = len(k)
#     dict_[k] = v
# print(dict_)


# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# list1 = list(dict_)
# list1.sort(key=len)
# print(list1[-1])

# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {}
# for k in dict1:
#     v = k ** 3
#     dict2[k] = v
# print(dict2)

# ct_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# for k, v in ct_.items():
#     for v2 in v.values():
#         ct_[k] = v2
# print(ct_)


list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
ls =[]
a = {}
list1 = []
list2 = []
for i in list_:
    ls.append(str(i))
for i in ls:
    if i.isalpha():
        list1.append(i)
    elif i.isdigi


