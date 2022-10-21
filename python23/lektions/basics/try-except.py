'========= Exeptions=============='

# isklucheni (oshibki)
# kogda nmy pytaensya ispolzovat metody ne cvoistvennye kakomu to ripy dannyh 
# ili kogda my putaemsya peredat funkcii bolshe ili menshe argumentav chem prinimaet funkcia


from multiprocessing.sharedctypes import Value
from re import X
from unittest import expectedFailure


SyntaxError
# isklucheie , kotoroe vyhodit, kogda v kode dopuchea cintakstecheskay oshibka  


NameError 
'iskluchenie, kotoror vyhodit , kogda my obrashaemsya k nesychestvyishei perenennoi '


IndexError 
' iskluchenie , kotoroe vyhodit , kogda my oroshaensya po ne sushesvyeshemy indexu'



KeyError 

#  iskluchenie , kotoroe vyhodit, kotoroe vyhodt kogda my  obrsjaemsa po ne sushestvyeshemy kluchu


ValueError 
''
TypeError
"""
for i in 12345678:

    ....
TypeError 'in' pbjectt id not iteravle

""" 

"""
5 + '5'
TypeError: unsuppeorted poerand typs(s) for 
"""


"======================================Exceptions======================================"
# Исключения (ошибки) - 

SyntaxError
# исключение, которое выходит, когда в коде допущенна синтаксическая ошибка
"""
(
SyntaxError: unexpected EOF while parsing
(когда мы не закрыли скобочку или кавычку)
"""

"""
a = 
SyntaxError: invalid syntax
(когда мы сделали что-то не правильно в синтаксисе)
"""


NameError
# исключение, которое выходит, когда мы обращаемся к несуществующей переменной
"""
slfdjhuksrgh.split()
NameError: name 'slfdjhuksrgh' is not defined
"""

IndexError
# исключение, которое выходит, когда мы обращаемся по несуществующему индексу
"""
list_ = [1,2,3,4,5]
list_[1000]
IndexError: list index out of range
"""

"""
[1,2,3,4,5].pop(1000)
IndexError: pop index out of range
"""

"""
[].pop()
IndexError: pop from empty list
"""

KeyError
# исключение, которое выходит, когда обращаемся по несуществующему ключу
dict_ = {'a':1}
# dict_['b']  - KeyError: 'b'
# dict_.pop('b')   - KeyError: 'b'

dict_.get('b')
# ошибка не выйдет, просто если ключа нет - вернется None


ValueError
# когда мы передаем в функцию не коректный для нее тип данных
# когда мы распаковываем итерируемый обьект на несколько переменных и кол-во переменных не совпадает с кол-вом элементов в итерируемом обьекте

"""
int('10d')
ValueError: invalid literal for int() with base 10: '10d'
"""

"""
a,b,c = [1,2]
ValueError: not enough values to unpack (expected 3, got 2)
"""


TypeError
# когда мы пытаемся использовать методы не свойственные какому-то типу данных
# или когда мы пытаемся передать функции больше или меньше аргументов, чем принимает функция

"""
for i in 12345678:
    ...
TypeError: 'int' object is not iterable
"""

"""
5 + '5'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

"""
'5' + 5
TypeError: can only concatenate str (not "int") to str
"""

"""
{[1,2,3]:"hello"}
TypeError: unhashable type: 'list'
"""

"""
input('hello', 1)
TypeError: input expected at most 1 argument, got 2
"""

"""
[].append()
TypeError: append() takes exactly one argument (0 given)
"""


ZeroDivisionError
# выходит при делении 0
"""
45 / 0
ZeroDivisionError: division by zero
"""

"""
3 // 0
ZeroDivisionError: integer division or modulo by zero
"""

"""
3 % 0
ZeroDivisionError: integer division or modulo by zero
"""


AttributeError
# выходит, когда мы обращаемся к несуществующему аттрибуту или методу обьекта (типа данных)

"""
[].replace('a', '')
AttributeError: 'list' object has no attribute 'replace'
"""

"""
''.pop()
AttributeError: 'str' object has no attribute 'pop'
"""

IndentationError
# выходит, когда мы не правильно используем отступы
"""
   a = 5
IndentationError: unexpected indent
"""

"""
for i in range(10):
print(i)
IndentationError: expected an indented block
"""



Exception 
#  isklychenie, kotoroe sozdak=li cto by ego vyzyvat

'=============vyzov isklucheni =================='
# raise NameError
# raise NameError('Ne vernyi kod')



'=====================Obrabotka isklucheni ================ '

# ctoby kod ne prekrqshal dvoy raboty , my mogem ispolzovat konstukciu try-exept, i obrabatyvat vyzvannoe iskluchenie 

try:
    #  kod , kotori vozmojno vyzevet oshibku
    num = int(input('vvedite chislo: '))
except ValueError: # oshibka kotorya a moget vozniknut 
    # kod kotoryi otrabaryvaat tolko eski oshibka vyzvalas
    print('vvedte chislo')
else:
    print('vvedite chislo', num)
    # kod kotoryi otrobotaet tolko esli niakaya oshba ne vyshla
finally:
        print('Do svydNIE')



# ' cALKULATOR====================='

# is_exit = False
# operations = ('+', '*', '-', '**', '/', '//')


# while not is_exit:
#     try:
#         num1 = int(input('Vvedite 1 chislo:'))
#         num2 = int(input('Vvediyte 2 chisl: '))
#         oper = input('Vvedite operaciu: ')
#         if oper not in operations:
#             raise Exception
#         if oper == '+':
#             print(f'{num1} + {num2} = {num1 +num2}')
#         elif oper =='-':
#             print(f'{num1} - {num2} = {num1- num2}')
#         elif oper == '*':
#             print(f'{num1} * {num2} = {num1 * num2}')
#         elif oper == '**':
#             print(f'{num1} ** {num2} = {num1 ** num2}')
#         elif oper == '/':
#             print(f'{num1} / {num2} = {num1 / num1}')
#         else:
#             print(f'{num1} // {num2} = {num1 // num2 }')
#         if input('vy hotite vyiti (y/n) ').lower() == 'y':
#             is_exit = 'y'
        
            

#     except ZeroDivisionError:
#         print('na 0 delit nelzya')
#     except ValueError:
#         print('vvedite chislo: ')
#     except Exception:
#         print('Takoi operacii net')


# n = int(input())

# dict_ = {i: i ** 2 for i in range(1, 501) if not i % n}

# print(dict_)


'Try except======================'

# task n1
# try:
#     num1 = input('enter anything: ')
#     num2 = input('enter anuthing: ')
#     result = int(num1)  + int(num2)
# except ValueError:
#     result = num1 + num2
# finally:
#     print(result)


# task 2

# dict1 = {1: 'Raichel1234', 2: 'Johnhello', 3: ' Alicequarty'}
# dict1 = {value: key for key, value in dict1.items()}
# print(dict1)

# try:
#     username = input('Enter username: ')
#     ID = dict1[username]
#     print(ID)
# except KeyError:
#     print('There is no such username in dataabase ')
# else:
#     print(f'welcome, {username}')
# finally:
#         print('Thank you')

# Task 3
# try:
#     age = int(input('Enter your age'))

#     if age <= 0:
#         raise Exception('Do not enter negetive integers or zero')
# except ZeroDivisionError:
#     print('your age under 0')
# except ValueError:
#     print('Enter integer, not a string')

# else:
#     print(age)

# try:
#     b = 10
#     c = 11
# except NameError:
#         print(str('Такой переменной не существует!'))
        
# print(a)

# try:
#     num1 = input('enter anything: ')
#     num2 = input('enter anuthing: ')
#     result = int(num1)  + int(num2)
# except ValueError:
#     result = num1 + num2
# finally:
#     print(result)

# try:
#     num1 = input('Enter please')
#     num2 = input('Enter please')
#     result = int(num1) + int(num2)
# except ValueError:
#     result = num1 + num2
# finally:
#     print(result)
# dict1 = {1: 'Raichel1234', 2: 'Johnhello', 3: ' Alicequarty'}
# dict1 = {value: key for key, value in dict1.items()}
# print(dict1)


# try:
#     username = input('Enter username: ')
#     ID = dict1[username]
#     print(ID)
# except KeyError:
#     print('There is no such username in dataabase ')
# else:
#     print(f'welcome, {username}')
# finally:
#         print('Thank you')
# try:
#     num1 = int(input())
#     num2 = int(input())
#     result = num1 + num2
#     print(result)

# except ValueError:
#      print('Введите число!')


# try:
#     dict_ = {'key1': 'value1', 'key2': 'value2'} 
#     print(dict_['key5'])
# except KeyError:
#     print('Нет такого ключа!')






# try:

#     age = int(input())
#     if age <18:
#         raise ValueError('Доступ запрещен')
# except (TypeError,ValueError):
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

 

'=========================================='


#  task 7
try:
    age = int(input())
    if age < 18:
        raise ValueError('Доступ запрещен')
except ValueError:
    # print(error)
    print('Введён некорректный возраст')
else:
    print('Спасибо')
finally:
    print('До свидания!')
'================================================'



# try:

#     num1 = int(input())
#     num2 = int(input())
#     result = num1 / num2
#     print(result)
# except ZeroDivisionError:
#     print('Произошла ошибка!')
# except ValueError:
#     print('Произошла ошибка!')



# try:
#     cash = int(input())
#     if cash < 0:
#         raise ValueError
# except ValueError: print('Сумма не может быть отрицательной!')
# else:
#     print(cash)
try:
    num1 = input('enter anything: ')
    num2 = input('enter anuthing: ')
    result = int(num1)  + int(num2)
except ValueError:
    result = num1 + num2
finally:
    print(result)