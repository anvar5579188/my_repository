# from traceback import print_tb


# db =[ 
#     ['Anvar', 15, 'Student'],
#     ['Beka', 28, 'mentor'],
#     ['Chopa', 18, 'mentor'],
#     ['Isman', 24, 'mentor'],]

# for person in db:
#     name = person[0]
#     age = person[1]
#     prof = person[2]
#     if age > 15:
#         print(f'Hello {name}, you are {prof}' )
#     else:
#         print(f'{name}, you are young')






# digits = [1,2,3]
# res = ''
# for i in digits:
#     res += str(i)

# res = str(int(res)+ 1)
# digits.clear()
# for i in res:
#     digits.append(i)
#     print(digits)


# nums = input('Введите семь чисел через запятую: ').split(', ')
# print(nums[0], nums.pop())
# nums.append('Makers')
# print(nums)


# g= (input('Vvedyte 7 chisel cerez zapyatuy: ')).split(', ')

# print(g[0],   g.pop())
# g.append('Makers')
# print(g)



# from random import randint
# num1 = []
# for n in range(10):
#     num1.append(randint(1,40))
# print(sorted(num1))


# from random import randint
# a = []
# for n in range(10):
#     a.append(randint(1,50))
#     print(sorted(a))

# words = input('vvedite spisok slov cherez zapyatyuy: ')
# length = []

# for i in words:
#     length.append(i)
#     print(f'')


# 3) Напишите программу, которая заполняет список словами, введенными 
# с клавиатуры, измеряет длину каждого слова и добавляет полученное значение в другой
#  список. Например, список слов – ['yes', 'no', 'maybe', 'ok', 'what'], список длин – [3, 2, 5, 2, 4]. \
#     Оба списка должны выводиться на экран.
# """

# words = input('Введите список слов через запятую: ').split(', ')
# lengths = []

# for i in words:
#     lengths.append(len(i))

# print(f'список слов - {words}\nсписок длин - {lengths}')
 


# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# tuples.pop()
# for i in tuples:


# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]

# for i in tuples:
#   if not len(i):
#     tuples.remove(i)

# print(tuples)

# for person in db:
#     name = person[0]
#     age = person[1]
#     prof = person[2]
#     if age > 15:
#         print(f'Hello {name}, you are {prof}' )
#     else:
#         print(f'{name}, you are young')






# name = input['']
# for i in range(5):
#     suarname = name[1]
#     print(suarname)


from termios import FIOCLEX


# fio = []
# for l in range(5):
#     fio1 = input().split()[-1]
#     fio.append(fio1)
#     fio.sort()
# print(fio)
# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# for x in list_:
    






# list4 =[2,3,4,3,4,3,5,6,5,6,2,2,2,2,287,8,8,8,8]
# print(list4.count(2))

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# # print(len(lists))
# print(lists.sort())
str_list = ['abc', 'xyz', 'aba', '1221']
indexes= []
for i in str_list:
  if i[0] == i[-1]:
        indexes.append(i.index(str_list))
print(indexes)




