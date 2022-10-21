
# ia = 10
# b = 5


# list1 = ['1', '2']

# list2 = []
# for i in list1:
#     if i == [0]:
#         i = '0'
#         list2 = i
    

# print(list2)



# a = {'a': 10, 'b': 9, 'c': 3}
# result= 1
# for key in a:    
# 	    result=result * a[key]
        	
# print(result)


# my_str = input(':')
# if my_str.isupper():
#     print(True)
# else:
#     print(False)






# points = int(input(':'))
# if points >100:
# 	print('ivinite takogo chisla net')
# elif points >=90 and points >100:
#      print('Отлично, Ваша оценка 5!')
# elif points >=80:
#     print('Отлично, Ваша оценка 4!')
# elif points >= 70:
#     print('Хорошо, Ваша оценка 3!')
# elif points >= 60:
#     print('Вам стоит подучить материал')
# elif points < 60:
#     print('Вы не сдали экзамен')


from sre_compile import isstring


number = int(input(':'))
if number <= -1:
	print('negetive')
elif number == 0:
	print('zero')
elif number >= 1:
	print('pozitive')
else:
	print('error')

