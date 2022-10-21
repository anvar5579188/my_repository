from curses.ascii import isalpha
from xml.sax.handler import property_interning_dict


friends = {
    'Мурату': 24,
    'Эржану': 21,
    'Чынгызу': 24,
    'Алтынай' :17,
    'Асеме': 16 
}

# for k, v in friends:
#   if v > 18:
#     print('dobro pogLOVt')
#   elif v <= 17:
#     print('dostup zakryt')
# print()
# a = [i for i in range(1,26, 2) ]
# print(a)
# list1 = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# list2 = [1 if i < 0 else  i for i in list1]

# print(list2)
# list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10] 
# list2 = [i for i in list1 if type(i) == str]
# print(list2)

# list1 = [0, 3, 9, 7, 5, 2, 18, 4]
# list2 = [i for  i in list1 if i > 5]
# print(list2)
# list1 = [False, True, False, True, False, True, False, True, False, True] 
# list2 = [int(i) for i in list1 ]
# print(list2)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# list2 = [len(name) for name in list_name]
# print(list2)

# b = [i for i in range(1, 1000, 125) if i % 2 ==0]
# print(b)



# list1 = [44,54,64,74,104]
# list2 = [6 + i for i in list1 ]

# print(list2)


# list1 = [2, 4, 6, 8, 10, 12, 14]
# list2 = [i for i in list1 if i ** 2 > 50]
# print(list2)

# list1 ="happy birthday!"
# list2 = [i for i in list(list1) if i.isalpha() ] 
# print(list2)

# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list2 =  [v for k,vk in dict_.items() for v in vk.values()]  
# print(list2)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# list2 = 
# print(list2)

# list_=[i for i in range(1, 100)]
# print(list_)

# list_ = [i for i in range(1,50, 3)]
# print(list_)

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [i for i in list_ if i > 0  % 2]
# print(int_list)

# list_ = [i ** 2 for i in range(1, 26) ]
# print(list_)

# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(i) for i in str_list ]
# print(int_list)

# list_ =[i**2 if i % 2 == 0 elsei for i in range(1,11)  ]
# print(list_ )

# list_ = [True if i % 2 == 0 else False for i in range(1, 11)]
# print(list_)

list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
print(list_name)