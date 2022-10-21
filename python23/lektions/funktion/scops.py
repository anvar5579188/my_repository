'==============================Oblast nevidinosti=============================='
#   LEGB- local enclosed global build-in
'============================Build- in============================'
# vstroennye prostranstvo inen

'========================Global========================'

# vse peremennue, kotorye my sozdaly vnutri odnoga faila 
# toby posmotret vse globalye peremennye, mojno ispolzovat globals 

# a = 5
# b ='hello'
# print(globals())


'===================================Encliosed==================================='

# zamknutae prostranstvo imen - lokalnoe prostranstvo 
# u kotorogo est vnurtrnneee l0kalnone prostranstvo 
# def func():
#     # lokalnoe prostranstvo dlya globalnogo prostranstvo 
#     #zamknutoe prostranstvo (potomy chto est molee lokalnoe prostranstvo )
#     var ='enclosesd'
#     def inner_func():
#         var = 'lokal'
#         print(var)
#     print(var)

# func(var)

        # lokalnoe prostranstvo dllya prostranstvo func

"================================LOcal================================"
 #lkalnoe prostranstvo imen - peremennye , sozdanie vnutri funkcii 

# a = 10 
# def func(a, b):
#     print(a, b)


# count = 10

# def incres_count():
#     global count
#     count += 1


# incres_count()
# incres_count()
# incres_count()
# incres_count()
# print(count)



def count(i):
    counter = 0

    def increase_counter():
        nonlocal counter
        # dostup na izmenenye peremennoi zamknutogo prostranstvo
        print(counter)
        counter += 1
    for _ in range(i):
        increase_counter()

count(11)