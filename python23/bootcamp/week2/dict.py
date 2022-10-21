# from operator import index


# a = {'x': 1, 'y': 2, 'z': 1}
# b = list( a.values())
# print(b[0])


# # >> d = {'a': 'Arthur', 'b': 'Belling'}

# # >> d.items()
# # [('a', 'Arthur'), ('b', 'Belling')]

# # >> d.keys()
# # ['a', 'b']

# # >> d.values()
# # # ['Arthur', 'Belling']
# # a = {'a': 1, 'b': 2, 'c': 1}
# # delated = a.pop('a')
# # print(delated)
# from pickle import APPEND
# from re import A
# from readline import append_history_file
# from traceback import print_tb
# # a = {'a': 1, 'b': 2, 'c': 1}
# # a['f']= 55
# # print(a)


# # a = {'a': 1, 'b': 2, 'c': 1}
# # b = list(a.values())

# # a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# # b = {}
# # for k, v in a.items():
# #     if  v % 2==0:
# #         b[k]=
# #     else:
# #         b[k]=v
# # print(b)




# # a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# # for k, v in list(a.items()):
# #     if v == None:
# #         del a[k]
# # print(a)

# # a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}

# # for  k, v in a.items():
# #     a[k] = v / 5

# # print(a)

# # a = {'apple': 2, 'orange': 5, 'banana': 10} 
# # b = a

# # for k, v in list(a.items()):
# #     if v % 2== 0:
# #         del a[k]
    
        
# # print(a) =====================================================       


# # a = {'a': 1, 'b': 2, 'c': 3} 
# # b = {}
# # for k, v in a .items():
# #     b[v] = k
# # print(b)



# # dict1 = {'a':1, 'b':2, 'c':3}

# # d = {}
# # for key, value in dict1.items():
# #          d[value] = key
         
# # print(d)


# # a = {'a': 3, 'b': 2}

# # print(sum(a.values()))




# # print(a['a'] + ['b'])


# a1 = {'q':1, 'a':2}
# print(a1)
# a2 = {}
# a2['s'] = 23
# a2['q'] = 20
# print(a2)
# cities = [('London', 'UK'), ('New York', 'US'), ('Tokyo', 'Japan')]
# d_cities = dict(cities)
# print(d_cities)

# a = {'a': 10, 'b': 9, 'c': 3}
# result= 1
# for key in a:    
# 	    result=result * a[key]
        	
# print(result)







# string1 = "pythonist" 
# newdict = {}
# for s in string1:
#     newdict[s] = string1.count(s)
# print(newdict)

# string = "pythonist" 
# dict_ = {}
# for s in string:
#     dict_[s] = string.count(s)
# print(dict_)

# def romanToInt(s: str) -> int:
#     # Dictionary of roman numerals
#     roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     # Length of the given string
#     n = len(s)
#     # This variable will store result
#     num = roman_map[s[n - 1]]
#     # Loop for each character from right to left
#     for i in range(n - 2, -1, -1):
#         # Check if the character at right of current character is bigger or smaller
#         if roman_map[s[i]] >= roman_map[s[i + 1]]:
#             num += roman_map[s[i]]
#         else:
#             num -= roman_map[s[i]]
#     return num


# s = "MCMXCIV"


# a = {
# 'I':1,
# 'V':5,
# 'X':10,
# 'L':50,
# 'C':100,
# 'D':500,
# 'M':1000
# }

# b = 0


# for k, v in a.items(list()):
#     if a == 0:
#         a + b
#     elif a < 5:
#         a + b - 1
#     elif a > 100:
#         a + b - 10
#     elif a < 1000:
#         a + b -100
#     elif a == 1000:
#         a +b

# print(a)
  

#   a = {
# 'I':1,
# 'V':5,
# 'X':10,
# 'L':50,
# 'C':100,
# 'D':500,
# 'M':1000
# }

# b = 0


# for k, v in a.items():
#     if a == 0:
#         a  == b
#     elif a < 5:
#         a == b - 1
#     elif a > 100:
#         a + b - 10
#     elif a < 1000:
#         a ==b -100
#     elif a == 1000:
#         a +b

    
  



# a = {
# 'I':1,
# 'V':5,
# 'X':10,
# 'L':50,
# 'C':100,
# 'D':500,
# 'M':1000
# }

# b = 0


# for k, v in a.items():
#     if a == 0:
#         a  == b
#     elif a < 5:
#         a == b - 1
#     elif a > 100:
#         a + b - 10
#     elif a < 1000:
#         a ==b -100
#     elif a == 1000:
#         a +b

    
  


# from tkinter import S


# roman = {
# 'M' : 1000,
# 'D' : 500,
# 'C' : 100,
# 'L' : 50,
# 'X' : 10,
# 'V' : 5,
# 'I' : 1
# }

# x = 0
# res = 0

# for i in [::-1]:
#     if roman[i] >= x:
#         res += roman[i]
# else:
#     res -= roman[i]
#     x = roman[i]


# print(res) 


a = {'a': 1, 'b': 2, 'c': 3} 
b = {}
for k, v in a .items():
    b[v] = k
print(b)
