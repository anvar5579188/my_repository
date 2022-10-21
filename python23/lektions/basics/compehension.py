'==========Comperhansions-=================='


# # comperhension = eto generator s pomoshyi kotoroga my mojem sozdavat posledevatelnosti iispolzyua cikl for v odnu ctroku 


# # rezutat for elememt in posledovatelsi 
# #  rezultat for element in pesedovatelnosti if filtr

# from ast import comprehension


# comprehension = (i for i in range (1,7))

# print(comprehension)
# #  generator eto iterioemyi obyekt kotoyi ne hranit v sebe polnostyi
# #  vsyi posledovatelnist dannyh a sozdaet kogda ana potrebyetsay

# print(next(comprehension))
# print(next(comprehension))
# print(next(comprehension))
# print(next(comprehension))
# print(next(comprehension))
# print(next(comprehension))
# print(next(comprehension))

#  next - eto fynkciya kotoraya zaprashivaet y generatora tekyshi element i generator spzdaet sledyisi element 
'===========cintaksitechski sahar================'

# list comprehension 
# list_comprehension = list ((i**2 for i in range(1, 6)))


# list_comprehension = [i**2 for i in range(1, 6)]
# print(list_comprehension)


# list_comprehension1 =[i  for i in range(1, 11, ) if i % 2 == 0] 
# # print(list_comprehension1)
# list3 = []
# for i in range(1,11):
#     if i % 2== 0:
#         list3.append(i)
# print(list3)


# list4 = []
# for i in range(5):
#     list4.append('hello')

# list2 =['hello' for _ in range(5)]
# print(list2)

' cozdat spisok ot 1 do 10 no  v meste chisel napisat chetnoe ili ne chetnoe'

# list = []
# for i in range(1, 11):
#      if i % 2== 0:
#         list.append('chetnoe')
        
# else:
#      list.append('ne chetnoe')
# print(list)



# list5 = ['chetnoe' if i % 2 == 0 else "ne chetnoe"
# for i in range(1, 11)]
# print(list5) 


# from turtle import pen


# dict1 = { i:str(i)  for i in range(1,11)  }


# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# list3 =[]



# list6 = [i for i in  [1, 'hello', 2, 'a', 2.3, 1000, 'makers'] if type(i) == str]
# print(list6)



'============Dict cpomprecension================'
# dict1 = dict((i, i **2) for i in range(10))
# print(dict1)

# dict2 = {i: i**2 for i in range(10)}



# dict1 = {'a':1, 'b':2, 'c':3}
# dict2 = { k:v for k v in dict1.items()}


# dict1 = {'a':1, 'b':2, 'c':3}
# dict2 = {value:key for key, value in dict1.items()}



# dict1 ={
#         'a':[1,2,3,4],
#         'b':[10,15,16,17],
#         'c':[1,2,54]
# }

# dict2 = {key:sum(value) for key, value in dict1.items()}
# print(dict2)




# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# list3 = {list1[i]: list2[i] for i in range(5)}
# print(list3)





'===================Praktica v Makers==================='


# list1 = []
# for num in range(1, 21):
#     list1.append(num *2)
# print(list1)

# list_comprehension
# list1 = [num * 2 for num in range (1, 21)]
# print(list1)
   
# list_users = ['alie', 'Sam', 'SAndy', 'Bowl']
# invetations = ['you are inveited ' + name for name in list_users]
# print(invetations)

# list1 = [10, 5, -6, -12, 20, 3, 14, 4]
# list2 = [num for num in list1 if num % 2 ==0 
# and num > 0 ]
# print(list2)

# strings = ['1998', '2001y', '2008year', '2020']
# list_ = [year for year in strings if year.isdigit()]

# print(list_)

# list1 = ['Raychel', 'John', ' Alice', 'Sam' ]
# list1 = [len(name) for name in list1]
# print(list1)

# list1 = [-4, -12, 0, 2, 5, 6, 4]
# list1 = [x if x < 0 else x ** 2 for x in list1]


'================== Vlogennyee coprehension============='



# list1 = {}
# for i in range( 1, 6):
#     key = i
#     value =[j for j in range(1, i + 1)]
#     list1[key] = value
        
# print(list1)

# # dict2 = [i: [j for j in range(1, i+1)] for i in range(1,6)]
# dit3  = { i: list(range(1, i+1)) for i in range(1, 6)}
# print(dit3)


# list3 = {'hello world' list(range(10)) for i in range(1, 6)}
# print(list3)

# list2 = [['hello world' for j in range(5)]for i in range(10)]
# list1 = [['hello world']* 5 for i in range(10)]


# list2 = [[  j for j in range(1,6)]for i in range(10)]
# print(list2)

# list1 = {}
# for i in range( 1, 6):
#     key = i
#     value =[j for j in range(1, i + 1) ]
#     list1[key] = value
#     for g in range(1, i + 1):

# print(list1)

# dict_ = {i: {j: list(range(1, j + 1)) for j in range(1, i + 1)} for i in range(1, 6)}

# print(dict_)

# dict1 = {}

# for i in range (1, 6):
#     inner_dict = {}
#     for j in range(1, i + 1):
#         list1 = []
#         for k in range(1, j+1):
#             list1.append(k)
#             inner_dict[j]=list1
#             dict1[i] = inner_dict
# print(dict1)



# dict_ = {1: 'hello', 2:'world'}
# dict_ = {k: len(v) if k%2==0 else len(v)**3 for k,v in dict_.items()}
# print(dict_)
from hashlib import new
from re import I

'===================================================================================================='
#  task 8


# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list  = [['longer'] if len(i)>=4 else ['shorter'] for i in list_name]

# print(new_list)



# dict_  ={i for i in range(1,11)  }


n = int(input())

dict_ = {i: i ** 2 for i in range(1, 501) if not i % n}

print(dict_)