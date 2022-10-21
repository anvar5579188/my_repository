# '================Funkcii=============='
# # funkcii - eto imennovannyi block koda, kotoryi moget prineamat argumenty  i vozvroshat rezultat


# # def my_sum(x, y):
# #     print(x + y)
# #     return x + y
# # res = my_sum(5, 6)
# # print(res)


# # def my_len(abj):
# #     count = 0
# #     for element in abj:
# #         count += 1
# #         #count = count +1
# #         return count
# # res = my_len(['abj',1,2,3])
# # print(res)


# ' Funkcii sobludayut princip DRY [dont repeat yourself ]'

# db = [
#     {'name':'hello', 'password':45918837},
#     {'name':'World', 'password':57918837}
#     ]

# def in_database(name):
#     for user in db:
#         if user ['name'] == name:
#             return True
#     return False


# def register(name, password1, password2):
#     if in_database(name):
#         raise Exception('yozer  takim imenem uge sushestvuet')
#     if password1 != password2:
#         raise Exception('password error')
#     user = {'name':name, 'password': hash(password1)}
#     db.append(user)
#     return "Register"


# def login(name, password):
#     if not in_database(name):
#         raise Exception('User not found!')
#     for user in db:
#         if user['name'] == name:
#             if user['password'] != hash(password):
#                 raise Exception('password not true!')
#     return'you have registret'
# # user = register('anvar', '1234', '1234')
# # print(login('anvar', '1234'))
# # db.append(user)
# # print(user)
# # print(db)
# # user = registr('elza', '2345678', '2345678')
# def main():
#     print('welcome')
#     while True:
#         try:
#             action = input('Registr:1' 'login:2' 'Exit:3\n')
#             if action =='3':
#                 break
#             elif action == '1':
#                 name = input('Enter name: ')
#                 p1 = input('Enter password: ')
#                 p2 = input('repeat passwort: ')
#                 print(register(name, p1, p2))
#             elif action == '2':
#                 name = input('enter name: ')
#                 password = input('Enter password: ')
#                 print(login(name, password))
#             else:
#                 print('Not correct')
#         except Exception as error:
#             print(error)

# main()



'argumenty i parametry'
  
# parametry = vnutri funkii , znacheniyzkitirym my zadaem pri vyzove 
# funkcii (peremennye, kotorye my poshem v kruglyg skobkah, kigdap poshen def )
#arguenty - znacjenya , koroye my peredaem pro vyzove 

'=========================Vydy parametrov ==================='
# 1 - OBYZATELNYE 
# 2 - NE OBZATELNYE 
# 2.1 - c defoltom (so znachenyem po umolchaneyi)
#2.2 - aregs (vsr pozocionnye argementy kotorye ne popali v obyazateluye i s defoltom )
#2.3 = kwargs (vs lishnei imennovanye argemnty )  

'========================Vydi argumenty================='

# 1 pozicionnue (po pozicii )
#2 imnovannye (po nazvanye (parametr = znaachenie))


# def add_or_add_10(num1, num2=10) -> int:
#     'ana skladyvaet dva chisla Esli vtoroe chislo ne peredat, slogit pervoe s 10'    
#     return num1+num2

# '------------------ *----------------'
# list1 = list(range(1,11))
# print(list1)

# dict1 = {'a':1, 'b':2}
# dict2 = {**dict1}
# print(dict2)
# list3 = []

# def funck(a, b=10, *args, **kwargs):
#     print('a-',a)
#     print('b-',b)
#     print('args-', args)
#     print('kwargs-', kwargs)




'===============Lamda================'
# lambda - eto anonimnaya finkciya, kotoraya v odnu stroku
# a = lambda x:x **10 
# print(a(5))
'kalkulyator s funkcii======================================'


# from pickletools import string1


calc = {
    '+': lambda num1, num2: num1 + num2,
    '-': lambda num1, num2: num1 - num2,
    '*': lambda num1, num2: num1 * num2,
    '/': lambda num1, num2: num1 / num2,
    '//':lambda num1, num2: num1 // num2,
    '**': lambda num1, num2: num1 ** num2,
     '%':lambda num1, num2: num1 % num2,
}
def main():
    try:
        num1 = int(input('Enter the number please: '))
        num2 = int(input('Enter the secod number: '))
        num3 = input('Enter the operation: ')
        funk = calc[num3]
        res = funk(num1, num2)
        print(num1, num3, num2, '=', res)

    except ValueError:
        print('Enter the number please!')
    except KeyError:
        print('operation is not true')
    except ZeroDivisionError:
        print('zero os out of opperation')



# mтвтыилтмжмin()

def translate(string:str)-> str:
    eng="qwertyuiop[]asdfghjkl;'zxcvbnm,."
    ru = "йцукенгшщзхъфывапролджэячсмитьбю"
    if string[0] in eng:
        dictionary = str.maketrans(eng, ru)


    else:
        dictionary = str.maketrans(ru, eng)
        return string.translate(dictionary)

print(translate('кутарврщ'))

'================Praktik Mkers ==================='


# def funktion():
#     print('The funktion is called')
#     return 'Makers'
# print(funktion())




# variable = substract()
# print(variable)
 
# list1 = [1,2,3,4,5, substract()]
# print(list1)


# def substract():
#     num1 = 20 
#     num2 = 5
#     print(num1 + num2)
#     return num1 - num2


# def funcktion():
#     print('I"m callig substrct')
#     variable = substract()
#     return variable
# print(funcktion())


# from logging import lastResort


# # def welcome(name, last_name):
# #     return(f'Welcome, {name} , {last_name}')
# # name = input(': ') 
# # last_name = input(': ')
# # print(welcome(John, snow))



# from csv import list_dialects


# def get_word(word):
#     list_letters = list(word)
#     print(list_letters)
#     return list_letters


# def get_vowels(letters):
#     vowels = ['a', 'o', 'y', 'i', 'e', 'u']
#     list_vowels = [letter for letter in letters if letter in vowels ]
#     result = ''.join(list_vowels)
#     print(list_vowels)
#     return result
# my_word = input('Enter the name: ')
# print(get_vowels(get_word(my_word)))





# def info(name, age):
#     return f'{name} is {age} years old.'
# print(info())


# #    *args    **kwargs
# # 
# def func(required, *args, **kwargs):
#     print(required) 

#     if args:
#         print(args)

#     if kwargs:
#         print(kwargs)

# func('Makers', 'Bootcamp', 'pyhon', name = 'Rychel', age = 23)
#
# 
'==========Task1====='
# 
# 
# def generate_password(p1, p2):
#     import random
#     random_list = random.sample(range(1, 10),k=7 )
#     random_list = [str(i) for i in random_list]
#     password = p1 + p2 + ''.join(random_list)
#     print(password)
#     return password



# def get_info(name=input('Enter yoyr name: '), last_name=input('Enter your last name: ')):
#     password = generate_password(p1 = name, p2 = last_name)
#     return password
# print(get_info())
'===========Task2==================='

# def get_data():
#     inp1 = int(input('Enter the first number: '))
#     inp2 = input('Enter the command:  ')
#     inp3 =int(input(' Enter the second number: '))
#     oper = ['+', '-', '/', '*']
#     if inp2 in oper:
#         if inp2 == '+':
#             return inp1 + inp3
#         elif inp2 == '-':
#             return inp1 - inp3
#         elif inp2 == '/':
#             return inp1 / inp3
#         elif inp2 == '*':
#             return inp1 * inp3
# print(get_data())

# def ickream(name, size, **kwargs):
#     print(f'You {name} iscream {size} size')
#     if kwargs:
#         print('Your toppings: ' + '\n')
#         for value in kwargs.values():
#             print(value)
# ickream(name = 'choclate', size= 'medium',
#         toppings = 'peants', toppings1 = 'choklate', toppins2 = 'cocao' )


# def add(a, b):
#     return a + b
# print(add(10, 2))


# def get_type(class1, class2):
#     return type(class1)
#     return type(class2)

# def dict_(my_dict):
#       for element in my_dict:
#           return dict(element)  
# d 

    # dict_ = {'a':1,'b':2}
    # def dictionary(x):
    #     for i in x.keys():
    #         print(i)



# def num(a):
#     if a % 2 ==0:
#         print('it is even number')
#     else:
#         print('It is odd number')
# num(6)

# def max_num(a, b):
#     return max(a, b)
# print(max_num(3, 8))

# def multiply_list(list1):
#     theSum = 0
#     for i in list1:
#         theSum = theSum + i
#     return theSum
# print(multiply_list(1,2,3,4,5,6))

# def multiply_list(iterable):
#      s = 0
#      result = []
#      for value in iterable:
#          s += value
#          result.append(s)
#      return result

# print(multiply_list())

# dict_ = {'x': 1, 'y': 2, 'z': 1}
# print(dict_.keys('x'))


# from curses import keyname


# dict_ = {'a': 1, 'b': 2, 'c': 1}
# del dict_['a']
# print(dict_)


# dict_ = {'a': 1, 'b': 2, 'c': 1}
# print(dict_.items())

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(max(dict_.values()))

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(sorted(dict_.values()))


# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# dict2  ={}
# for k, v in dict1.items():
#     if v % 2!=0:
#         dict2[k] = 1
#     else:
#         dict2[k] = v
# print(dict2)

# from os import popen


# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# dict1 = dict_.copy()

# for k, v in dict_.items():
#     if type(v) == int:
#         dict1.pop(k)
        
# print(dict1)

        
# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}
# for k, v in dict1.items():
#     dict2[k**2] = v 
# print(dict2)


# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = dict.fromkeys(list_)




# dict_.items()
# print(dict_)

    



# dict2 = {key:sum(value) for key, value in dict1.items()}
# print(dict2)

# string1 = 'anvar'
# string2 = 'kot'

# print(string1,string2)

# strng = 'Ilias kot'
# print(string)

# string = 'The quick brown fox jumps over the lazy dog'
# string1 = string.replace('o', '*')
# # print(string1)
# string = 'БЕГИ ФОРЕСТ, БЕГИ!'
# priint(string.lower())






from ntpath import join


# string = 'hello'
# i = list(string)
# i[-1], i[0] = i[0], i[-1]
# d = ''.join(i)



# print(d)

# hashtags = '#makers#bootcamp#программирование#it#курсы'
# i = list(hashtags)
# i.pop(0)
# d = ''.join(i)
# print(d.split('#'))

# name = input()
# last_name = input()
# age = input()
# city = input()
# print(f'Вас зовут {name } {last_name},  Ваш возраст:{age}, Вы проживаете в городе {city}')



# string = 'Makers bootcamp' 
# d = list(string)
# if d[0:15] % 2==0:
#     print(d)





# string = 'abracadabra'
# str1 = [str]
# string[5] = 'K'
# print(string)



def numbers(num1, num2, num3):
    num3 / (num1 + num2)
    if num3 == 0:
        print(num1 + num2)


numbers(34, 34, 9)
