# #'=============Slovary =================\'
# #  dict = izmenyemyi tip dannyh, neyporadocnny. neindexrovanyi tip dannyh, dlya hranenya dannyh v parah[kluch; znachebya ]


# # user = {

# #         'name': "Nastya",
# #         "age": 13,
# #         "last name": 'Tuz'
# # }


# # print(user['name'])  #'Nastya'



# # #kluchamy v slovare mogut byt tolko ne uzmenyamye typi dannyh 

# # # dict1 = {'a':1, 'b':2, 'a':3, 'a':4}
# # # print(dict1['c']) #KeyError 'c'






# # # "===========================Sozdanye======================="


# # # dict1 = {'a':1, 'b':2}
# # # diict2 = dict( [ ('a', 1), ('b', 1) ] )
# # # dict3 = dict(['ab', 'cd', 'ef'])


# # dict4 = {}
# # dict4 ['name'] = 'Nastya'
# # dict4['age'] = 13
# # print(dict4)

# # "=====================Metody slovorya=================="
# # #  get -= metod kotoyi cozvroshaet znachene po kluchu, esli takogo klucha net, to vozvroschaet None ili defoltnoe znachenie 

# # user = {
# #         'name': "Nastya",
# #         'age': 15,
# #         'lasst name': 'Tuz'
# # }

# # #user['id] KayError



# # # user.get('id') #None

# # # user.get('name')# 'Name'
# # # user.get('id', 1) # 1
# # # user.get('name', 'User') # Nastya


# # # # pop - udolyaet paty po kluchu i vazvroshaet znachenie 
# # # dict1 = {'a':1, 'b':2,  'c':4}
# # # popped = dict1.pop('a')
# # # # dict1 = {'b':2. 'c':4}


# # # popitem - udolyaet poslednyu paru i vozvroschaet ee

# # # dict1 = {'a':1, 'b':2,  'c':4}
# # # popped = dict1.popitem()
# # # print(dict1, popped)


# # #dict1 = {'a':1, 'b':2,}
# # #popped{'c':4}

# # # # update - raschiraet slovaar parami iz vtorogo slivarya 
# # # dict1 = {1:'a', 2:'b'}
# # # dict2  = {2:'c', 3:'d'}
# # # dict1.update(dict2)
# # # print(dict1) # 

# # # # clear- ochishaet slovar
# # # dict1.clear


# # #fromkeys - eto metd dlya sozdanie novogo slivorya ispolzuya sposok kychei


# # from re import A


# # dict1 = dict.fromkeys('hi')
# # dict2 = dict.fromkeys([1,2,3])



# # dict3= dict.fromkeys([1,2,3], 'Hello')
# # print(dict3)



# # keys - metod kotori vpzvrshaet kluchi 
# # values - metod kotorui vozvroshaeet znachenie 
# # items - metod kotoryi vozvroshaet pary klych - znachenie v vide tuple 
 


# # user = {

# #         'name': "Nastya",
# #          "age": 13,
# #          "last name": 'Tuz'
# # #  }
# # print(user.keys())
# # print(user.values())


# # print(user.items)


# # for key in user.keys():
# #         print(key)
# # pri iteracii slovarya budut prihodit klychi 


# # for items in user.items():
# #         print(items)
# # # items[0]= klych
# # #items[1] - znachenie 
# # # pri itercii dict_items priihodyat pary tuple

# # items = ('name', "nastya ")
# # key, value = ('name', 'NastyA')

# # for key, value in user.items():
# #         print(key,value)



# # dict1 = {'a':1, 'b':2, 'c':3}

# # d = {}
# # for key, value in dict1.items():
# #         d[value] = key
# #         print(d)





# # 'keys - metod kotori vpzvrshaet kluchi 
# # values - metod kotorui vozvroshaeet znachenie 
# # items - metod kotoryi vozvroshaet pary klych - znachenie v vide tuple 
 

# # slovar  = {1:'a', 2:'b', 3:'c'}

# # d = {}
# # for key, value in slovar.items():
# #         d[value] = key

# # print(d)


# from multiprocessing.sharedctypes import Value


# # a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
 
# # list_ = {
# #   'milk':4,
# #   'bread':4,
# #   'chocolate':10,
# #   'juice':123
# # }
# # basket = {}
# # for key, value in list_.items():
# #   if len(list_) != 0:
# #     basket[key] = value
# #     list_.pop(key)
# #   else:
# #     print(basket)  
# #     print(list_)


# # a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

# # for value in a.value():
# #         if value > None:
# #                 a.pop
# # print(a)





# # a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# # b = {}
# # for key, value in a.items():
# #   if value == None:
# #    b[key] = value

# # print(b)


# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# a = {}


# for i in list_:
#   length = len(i)
#   a[i] = length
# print(a)



# # a = {}
# # for i in list_:
# #   length = len(i)
# #   a[i] = length
# # print(a)

# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# a = {}






# from optparse import Values


# a = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# c = max(a.values())

# for k,v in a.items():
#         if v == c:
#                 print(k)


# "Дан словарь a, где ключами будут цены товаров, а значениями их названия, 
# затем пройдитесь циклом по нему и поменяйте все ключи элементов, 
# возведя их в квадрат, новые элементы запишите в словарь b


# a = {25: 'apple', 26: 'orange', 27: 'banana'} 
# b = {}
 
# for k, v in a.items():
#         b[k**2] = v

# print(b)


# a = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
# b = {}

# for k, v in a.items():
#         b[k] = v**3

# print(b)



#  Вы идете в магазин за продуктами. У вас есть список продуктов, в котором перечислены наименования продуктов и количество. 
#  Каждый раз, когда вы кладете тот или иной продукт в корзину, вы убираете этот продукт из списка. 
#  После того, как ваш список опустеет, вы идете к кассе и расплачиваетесь. Реализуйте данную задачу в вашем коде.
# * Используйте все знания, которые вы получили



# market = {
#         'meat':25,
#         'snack':15,
#         'soda': 30,
#         'clothes':6,
# }
# bucket ={}
# print(market)
# print(bucket)


# for k, v in market.copy().items():
#         bucket[k] = v
#         market.pop(k)

# print(bucket)
# print(market)


list_ = {
  'milk':68,
  'bread':78,
  'chocolate':34,
  'juice':90
}
basket = {}
print(list_)
print(basket)
for key, value in list_.copy().items():
  basket[key] = value
  list_.pop(key)
  print(list_)
  print(basket)  
print()
