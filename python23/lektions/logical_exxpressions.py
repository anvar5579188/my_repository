# =================Logicheskie i uslivnyel operaatory==============
#  logicheskie opeerati=ory = vyragenya kotorye vozvroshyaet True, esli vyrajenie False - esli ne verno 

# #  RAVENSTVO 
# from operator import ilshift


# 5 == 5 # true 
# 4 == 5 #false 

# #  ne ravenstvo 


# 4 != 5 # true 
# 5! = 5 # false 
 

# 'bolsche '

# 5>4 # true
# 5>10 # false 
# 5>5 #bfalse
# ' Menche'

# 5 < 4 # false
# 5 < 10 # true 
# 5 < 5 # false
# ' menshe ili rovno'

# 10 <= 5 # false 
# 5 <= 10 #true 
# 5 <= 5 # true 
# '5' == 5 # false 
# 'hello' == 'hollo' #true 
# 'Hello' == 'hello' # false 



# '====================And or not======================'


# #and = i 
# #  or = ili 
# # not = net
# a = 5 
# b = 6 

# #  trrue or and true 
# a == 5 and b == 6 # true 

# #True and False 
# a == 5 and b == 5 # False 
 

#  # false and false 

#  a = 4 and b = 4 # false



#  # Esle vse chasti vyragenya vozvroshaet     True - budet true 
#  # esli hotya by odn hast vyragenya False - budet Fase 





# # true or true 

# a == 5 or b = 5  # true 
#  # true and False 
#  a == 5 or b == 5  # true 

#  # false or Dalse 

#  a == 4 or  b == 4 # false 


# # Esli hotya by odn CHst vyrGENY vozvroshyaet True - budet true 

# not True # false 
# not False # True 
# not a == 5 # False [potomy cto a ==5 ]
# not a == 4 # True 


# '======================Boolean Type================'

# # Bulevyu typ dannyh imeet vsego 2 znahenya  True i False 

# bool(1) # True 
# bool(0) #False
# bool(-122) # true 


# bool('hello') #true 
# bool(' ') # true 
# bool('') # TRue 
# bool('True') # true 
# bool(False) # false 
  


# '=========================== NOne Type ================'
#  # None = neizmenyaemyi tip dannyh c odnim znacheniem  None, kotoryi ispolzyetsya dlya oboznachenya pustaty, otsutstvie znachenya

# bool(None) # False 
# bool('None') # True - potomu chto eto strok 

# a = None
# a is None  # true (is =eto proverka na polnoe sootvetstvie , vklychaya typ dannyh) 

 
# '========================= Uslovnye operator==================='
# # uslovnye operatory - konstrukciya, kotoraya used dly togo ctoby pri raznyh vhodnyh dannyh kod rabotal po raznomu (v zavisimosti ot usloviya)


# # if = uslovie1:
# #         telo1
# #         # telo1 budet vypolnyatya tolko esli ysllovie1 verno
# # if False:
# #             print('rabotaet')

# # if uslovir1:
# #     telo1
# #         telo 1 budeet vypolnyatsa tolko esli uslovie1 verno 
# # else:
# #     telo2
# #     # telo budet vypolnyatsa vo vseh drugi sluchayah


# if uslovie1:
#     telo1
# elif uslovie2:
#     telo2
#     #esli eslovie telo2 buet vypolnyatsa esli uslivie1 ne verno i esli  uslivie 2 verno



# if uslovie1:
#     telo1
# elif uslovie2:
#     telo2
# else:
#     telo3 
#     # telo 3 budeet vypolnytsa tolko esli vse vychukazennye  uslovia ne vernye 
#     # v odnooi konstrukcii my mojem ispolzovat tolkoo odin 'if' 
#     # v odnoi konstrukcii my mojem neogranichennoe kolichestvo (elif) ilo ne ispolzovaat voobsche 
#     # v odnoy konstrukcii toolko odine else ili ne ispolzvat voobshe 
#     #                




# num = int(input("enter date : "))
 
# if num > 0:
#     print(f'chislo {num} - pologitelnoe')
# elif num ==0:
#     print(f"chislo {num} - eto 0")
# else: 
#     print(f"chislo {num} - otricatelnoe")



# '======================ternarnye operatory=================='
# #  ternarnye operatory -  uslovie v odnu stroke 
 

# telo1 if uslovie else telo2

# num = int(input())
# res = 'Hello' if num == 5 else "bye"
# print(res)

# num = int(input())
 
# if num % 3 == 0:
#         print(f'Fizz {num} - kratno 3 ')
# elif num == 0:
#         print(f"buzz {num} - kratno 5")
# else: 
#     print(f"FizzBuss {num} - kratno 3 i 5 ")
#    '==========FiizzBuss==================
# '
# num1 = int((input()))
# if num1 in range (1, 100):
#     print('This is digit')
# elif num1 :
#     print('This is alpha')


# elif lang == 'ru':
#     print('thi is russia')
# elif lang == 'kg':
#     print('бул кыргыз тили ')
# elif lang == 'de':5
#     print('Das ist Deutch')






# elif num % 3 == 0:
#     print('Fizz')
# elif num % 5 == 0:
#     print('Buzz')
# else:
#     print(num)






# for num in range(1,101):
#     if num % 15 == 0: 
#         print('FizzBus')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)






# a ='1, 2, 3, 4, 5, 6'
# summa1 = int(a[0]) + int(a[3]) + int(a[6])
# summa2 = int(a[9]) + int(a[12]) + int(a[15])
# print(summa1 == summa2)







# a = int (input('Please enter the number: '))
# b= int (input('Please enter the number: '))
# c= int (input('Please enter the number: '))
# if a > b > c:
#     print(c, b, a)
# elif a > c > b:
#     print(b, c, a)
# elif b > a > c:
#     print(c, a, b)
# elif b > c > a:
#     print(a, c, b)
# elif c > a > b:
#     print(b, a, c)
# else:
#     print(a, b, c)



#Запросите у пользователя возраст и если этот возраст меньше 18, то выведите сообщение 'Доступ запрещен', в ином случае сообщение 'Добро пожаловать

# a = int (input('Please enter your age'))
# if a <18:
#     print('Dostup zakryt' )
# else:
#     print('Welkome') 


# Запросите у позьзователя число от 1 до 12
# Если число вне диапазона, выведите               
# Иначе выведите какому сезону принадлежит месяц под этим номером ("зима", "весна", "лето", "осень").

# a = int(input('Please enter nummer: '))
# if a >0 and a<3 or a==12:
#     print('Winter')
# elif a >2 and a<6:
#     print('Spring')
# elif a >5 and a<9:
#     print('Summer')
# elif a >8 and a<12:
#     print('Outumn')
# else:
#     print('takogo chisla net')
    
    
    
    # Запросите у пользователя строку
# Если строка состоит только из чисел, то выведите "is digit"
# Если строка состоит только из букв, то выведите "is alpha"
# Если строка состоит только из символов (! № ; % : ? * , . / < > - + =), то выведите "is symbol"
# В остальных случаях выведите "is ASCII"


# from curses.ascii import isalpha
# from cursesascii import issymbol 


# tring = input()
# if string.replace('-', '').isdigit():
#     print('is  digit')
# elif string.isalpha():
#     print('is alpha')
# elif string == '!' and string == '@' and string == '#' and string == '?':
#     print('is symbol')
# else:
#     print('is ASCII')
 #   а уроке физкультуры тренер говорит «на первый-второй рассчитайтесь». Запросите у пользователя номер человека. Что он скажет, «первый» или «второй»?
#


# num = int(input())
 
# if num % 1 == 0:
#          print(f'nomer {num} - pervuy')
# elif num % 2 ==0:
#     print(f'nomer {num} - vtoroy') 


# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1 - x2) == abs(y1 - y2):
#     print('YES')
# else:
#     print('NO')

# n = int(input())
# if n >= 11 and n <= 14:
#         print(n, 'korov')
# else:
#         temp = n % 10
#         if temp == 0 or (temp >= 5 and temp <= 9):
#                 print(n, 'korov')
#         if temp == 1:
#                 print(n, 'korova')
#         if temp >=2 and temp <=4:
#                 print(n, 'korovy')




# password = input('Введите ваш пароль: ')

# if not password.isdigit():
#   print('Ваш пароль должен хранить только числа')
# elif not len(password) >= 8:
#   print('Ваш пароль должен содержать не менее 8 символов')
# else:
#   print('Ваш пароль сохранен')

# tootal = (input('Введите свои баллы по математике, английскому языку и литературе через запятую: '))
# num1 = int(total[0:2])
# num2 = int(total[4:6])
# num3 = int(total[8:10])
# total1 = (num1 + num2 + num3) / 3
# if total1 >= 69:
#   print(f'Вы допущены к экзаменам. Ваш средний балл составляет {total1}')
# else:
#   print(f'Вы не допущены к экзаменам. Ваш средний балл составляет {total1}')


# total = (input('Enter your points from Math, Englisch and literature: '))
# num1= int(total[0:2])
# num2 = int(total[4:6])
# num3 = int(total[8:10])
# total1 = (num1 + num2 + num3) / 3 
# if total1 >= 69:
#     print(f'You are allowwed to take the exam. Your GPA is {total1}')
# else:
#     print(f'You can not to pass the exam. Your GPA is {total1}')
    


# import random

# comp = random.randint(1, 3)
# player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
# if player == 1:
#   print('Вы выбрали камень')
# elif player == 2:
#   print("Вы выбрали ножницы")
# elif player == 3:
#   print("Вы выбрали бумагу")

# if comp == 1:
#   print('Компьютер выбрал камень')
# elif comp == 2:
#   print("Компьютер выбрал ножницы.")
# elif comp == 3:
#   print("Компьютер выбрал бумагу.")
# if player == comp:
#   win = 0
# if player == 1 and comp == 2:
#   win = 1
# if player == 1 and comp == 3:
#   win = 2
# if player == 2 and comp == 1:
#   win = 2
# if player == 2 and comp == 3:
#   win = 1
# if player == 3 and comp == 1:
#   win = 1
# if player == 3 and comp == 2:
#   win = 2
# if win == 0:
#   print('Ничья!')
# if win == 1:
#   print('Вы победили!')
# if win == 2:
#   print('Компьютер победил!')

import random


comp = random.randint(1, 3)
player = int(input('1  - stone, 2- scissors, 3 - paper. '))
if player == 1:
    print('you have chose stone')
elif player == 2:
    print('you have chose scissors') 
elif player == 3:
    print('you have chose paper') 


if comp == 1:
    print('comp have chose stone')
elif comp == 2:
        print('comp have chose scissors')
elif comp == 3:
        print('comp have chose paper')

if player == comp:
    win = 0 
if player == 1 and comp == 2:
    win = 1 
if player == 1 and comp == 3:
    win = 2
if player == 2 and comp ==1:
    win = 2
if player == 3 and comp == 3:
    win = 1 
if player == 3 and comp == 2:
    win = 2 
if win == 0:
    print("nichya") 
if win == 1:
    print('You win!') 
if win == 2: 
    print('com[ win!') 
