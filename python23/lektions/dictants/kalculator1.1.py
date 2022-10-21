


# num1 = float(input('enter the number: '))
# num2 = float(input('enter the number: '))
# operation = input('chose the operation +-*/%**// : ')


# if operation == '+':
#     print(f'Rezultat slogenya: {num1 + num2}')
# elif operation == '-':
#     print(f'Rezultat vychetanya: {num1 - num2}')
# elif operation == '*':
#     print(f'Rezultat umnogenya: {num1 * num2}')


# elif operation == '/':
#     print(f'Rezultat delenya: {num1 / num2}')
    
# elif operation == '%':
#     print(f'Rezultat ostatka ot delenya: {num1 % num2}')

# elif operation == '**':
#     print(f'Rezultat delenie vozvedenya v stepen: {num1 ** num2}')
# elif operation == '//':
#     print(f'Rezultat delenya bez ostatka: {num1 // num2}')

# if num1 == 0:
#     print('na nil delit nelzya')


# else:
#     print('Operacia nevozmogno')
    






    #eval  = et kak funkciya kotoray prinimaet stroku i vypolnyaet ee kak kod

# code = 'print(10' 
# eval(code)

code = input('Vvedite chislo : ').replace(' ', '')

print(eval(code))
if '0/' in code:
    print('Na 0 delit nelzya')
else:
    print(eval(code))
    