#cikly 
# 










# banned = input(' Vrdite zapreshennye slova cherez zapyatuy: ').split(', ')
# text = input('vvedite text:')
# for word in banned:
#     if word in text:
#         text = text.replace(word, ' *')

# print (' Ispravlennyi text:')
# print(text)




name_of_list = ['Helloworld!']

length = len(name_of_list[0]) + 1
string = name_of_list[0]
string = string[length // 2:] + string[:length // 2]
result = list(string)

print(result)