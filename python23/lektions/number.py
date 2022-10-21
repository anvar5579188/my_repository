'===========chisla==============='
# # integer (int)= eto celye chisla 
# a = 5
# print (type(a))

# # c = int('10a')

# # float 
# a = 10.5
# print(type(a)) 

# ===========ssstroki===============



# ==========Eksranizaicya strok===========

# '\n' = eto perenos v novuy stroku

# print('hello\nworld')
# '\t'  = tobulyacya 
#print('hello\tworld')

# '\''#=eto otobrogenie
# '\\'
# print('\\')
'\v' # - eto perenos na novuy stroku so smesheniem v pravo na dlinu prededishey 

# print('hello\v world')

'\r' # = perenos koretki na nachalo stroki 



# print('hello world\rHI')


# print('hello woorld\rHi makrs')


' ==================Formatirovanie strok==============='


# # title = 'Iphone 14'

# # price = 150
# # format1 = f'Nazvanie: {title}\nCena: {price}'
# # print(format1)





# # format2 = 'Nazvanie:{}\nCena: {}'
# # print(format2.format("Hleb", 20))
# # print(format2.format("Chelovek", 200))




# # format3 = 'Nazvanie:  %s\nCena: %s'
# # print(format3 % ('iphone', 345))



# # ==================='Metody======p=========

# #  METODY = eto funkcii, kotorye otnosytsy k opredelennomy klassu[typy dannyh]
# # k nim my obroshyaemsya cherez tochky
# # 
# # 
# dir(str)#= posmotret vse metpdy klassa 


# 'HELLO'.lower()#'hello'
# 'hello'.upper() #;HELLO
# 'HeLLo' .swapcase()# hEllO

# 'hello world'.title()#'Hello Wolrld

# 'hello world'.capitalize()#'Hello world 

# 'hello'. center(11) #'      hello      '


# 'hello'.center(11, '-')#'-----hello---'

# 'hello world'.count('l') #3

# 'hello world'.count('ll') #'1'
# 'hello world'.count('makers') #0

# 'hello world' .startswith('hello')  #True

# 'hello world' .startswith('H') #false

# 'hello world'.endswith('ld') # true
 
# 'hello world' .islower() #true
# 'Hello world' .islower() # False

# 'HELLO'.isupper()  # True

# '1233' .isdigit()  #True
# 'hello' .isalpha()  #true\
# 'hello 1' .isalpha()  # False
# '12345' .isalnum() # TRue

# 'h1' .isalnum ()  # false


# 'hello wirld' .split()  # ['hello', 'world']
# 'hello world' .split('o')  # ['hello', 'w', 'rld']


# '-' .join(['hello', 'world'])  # hello-world
# ' ' .join(['hello', 'world'])  # 'hello world 
# '' .join(['hello', 'world']) # helloworld

# string1 = '                             12    hello                   '

# string1.string# '12 hello'

# string2 = '#hvr;bvjfbdvjbavbr$$$$$$'
# string2.strip('$')


# string1.lsstrip()  #'12    hello          '
# string.rstrip()  # '                               12      hello'
# ``




'========================Indeksy==============='
# indeks eto porytovuy nomer elementa v posledivatelnosty   simvalo v stroke \\


' h e l l o   w o r l d '
# 0 1 2 3 4 5 6 7 8 9 10
#                -3-2 -1 

# string = 'hello wold '
# string[0] # = h
# string[10] # = d
# string[5] # ' '
# string[-1] # d

# # ? strez - eto podstroka stroki
# string[0:5]
# string[6:10] # worl
# string[6:] # world
# string[ :5] # hello
# string[ : ] # hello world


# string[::2] # 'hlwrd4
# string[1:5:2]  # 'el
# string[::-1]  # dlrow olleh
# string[::-2]  #drwolh


# immatable_string = 'hello'
# print(immatable_string.upper())
# print(immatable_string)


# name = input()
# print(f"Hello {name}")




# string = input()
# print(f"hello")



# string1 = 'Hello'
# string2 = 'World'
# print (string1, string2)



# num1 = int(input('Menya zovut:'))

# num2 = int(input('Moy vozrast:'))
# print(num1)
# print(num2)


# name = input('name: ')
# suarname = input('suarname:')
# age = int(input('age: '))
# print(name)
# print(suarname)
# print(age)

s1 = 'America'
s2 = 'Japan'
s = s1[0]+s2[0]+s1[len(s1)//2]+s2[len(s2)//2]+s1[-1]+s2[-1]
print(s)