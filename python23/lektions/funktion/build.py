# '=====================Vsstroennye funkcii====================='

# # map, filter, reduce, zip, enumerate

# # zip ---- soedinyaet neskolko posledovatelnastey , (poluchaen gineratore v kotoreom elmenryty eto typle)

# # list1 = [1,2,3,4,5]
# # list2 = ['a', 'b', 'c']
# # list3 = [10.5, 20.6, 30.8 , 40.7]
# # zipped = zip(list1, list2, list3)
# # print(zipped)
# # for el in zipped:
# #     print(el)
# # # (1, 'a', 10.5)
# # # (2, 'b', 20.6)
# # # (3, 'c', 30.8)

# # list1 = [1,2,3,4,5]
# # list2 = ['a', 'b', 'c', 'd', 'e']
# # dict1 = dict(zip(list1, list2))

# # print(dict1)



# '============================enumerate============================'
# # enumerate - numeruet posledivatelnost (po defoltu s 0)

# import enum


# enumerated = enumerate('hellp world')
# print(enumerated) # <enumerate object at 0x7f30422bddc0>

# for el in enumerated:
#     print(el)
# # #(0, 'h')
# # (1, 'e')
# # (2, 'l')
# # (3, 'l')
# # (4, 'p')
# # (5, ' ')
# # (6, 'w')
# # (7, 'o')
# # (8, 'r')
# # (9, 'l')
# # (10, 'd')




# string = 'hello world'
# print(list(enumerate(string[5:])))


# '===========================map==========================='

# # map - prinemaet funkcii i posledovatelnost (zapisovaet v novyu posledovatelcnost 
# # rezultat funkcii, v kotoryu peredatsya elementy posledovatelnosti)

# list1 =['1', '2', '3', '4', ]
# mapped = map(int, list1)#<map object at 0x7fdcb115bf70>

# print(list(mapped))


# string = 'Hello world'
# res =''.join(map(lambda x:x.upper(), string))  #HELLO WORLD

# print(res)


# list1 = [1,32,3,4,5]

# print(list(map(lambda x: x**2, list1)))



# #  filter - vozvroshaet generator c elementmi, proshedshimi filtr (kakoe to uslove)

# list1 = [3, -5, 0, 10, -34]
# filtered = filter(lambda x: x>0, list1) #<map object at 0x7fdcb115bf70>

# print(list(filtered))

# users = [
#     {'name':'Anvar', 'age':3},
#     {'name':'Makers', 'age':45},
#     {'name': 'Sake',  'age':45}
# ]

# filter1 = filter(lambda x: x['age'] > 12, users)
# print(list(filter1))



# # vyvesti tolko imena 

# filter1 = map(lambda g: g['name'],filter(lambda x: x['age'] > 12, users))
# print(list(filter1))


'==========================redice=========================='

#  redice - prinimaet funkciyu i posledovatelnost, vozvroshaet 1 rezultat
#(peredavaya funkciy dilgna prinimat 2 argumenta)
# from functools import reduce
# list1 = [1,2,4,5,7,10,6]
# res = reduce(lambda x,y:x*y ,list1)
# print(res)



# string = 'hello'
# res = reduce(lambda x, y:x+'$'+y, string)

 # 'h$e$l$l$o'
# x = 'h', y = 'e' -> 'h$e'
# x = 'h$e', y = 'l' -> 'h$e$l'
# x = 'h$e$l', y = 'l' -> 'h$e$l$l'
# x = 'h$e$l$l', y = 'o' -> 'h$e$l$l$o'



# list1 = [1,2,3,4.6,5, 56,-1, -34]

# res = reduce(lambda x,y: x if x<y else y, list1)
# print(res)
from functools import reduce



users1 = [
    {'name':'Naastya', 'age': 23},
    {'name':'Makers', 'age':43},
    {'name': 'ilchik', 'age': 25}

]


res = reduce(lambda x,y: x if x['age']<y['age'] else y, users1)
print(res['name'])
