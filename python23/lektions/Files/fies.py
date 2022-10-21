'==================Moduli oakety=================='
# lyboi fail - eto modul c rashireniem .py - modul
#paket - nabor modulei (obyazatelno diljen byt fail _iniy_py
  


'==========================Rabota s failami=========================='


# open - funkciya kotaraya otkryvaet fail v opredelennom regime 
'regimi'

# r - read (tilko dlya chtenya)
# w - write (tolko dllya zapisi , kagdyi raz ochishaet)
# a - append (tolko dlya dozipisi, dobovlyaet v konec)
#x - sozdaet fail, no pri uslovii eslli on ne sushestvyet 
# b - binary (v binarnom vide )



file = open('test.txt', 'r')
# print(dir(file))
print(file.writable())  #false regim read
print(file.readable()) # true
print(file.read())
print(file.read())   # '' potonu cti koretka nahoditsya v konce

file.seek(0)  # perenos karetki na nachalo
print(file.read()) #r = 'hello' i td potomy  chto koretka nahoditsya na nulevom na 0 indexe 

file.seek(0)
print(file.read(3)) # (chitaem 3 simvola)
print(file.read(3)) # 'lo/n' (chitaem eshe  3 simvola)


file.seek(0)
print(file.readline()) # chitaet odnu stroku 
print(file.readline())
print(file.readline()) # '' (potomy chto kiretja nahoditsy v konce)

file.seek(0)
print(file.readlines())
print(file.tell()) # 39
 


file.close()
'============================Write============================'
file = open('new_file.txt', 'w')
# esli faila net on  sozdast ego 
print(file.readable())   # False (moget tolko zapisovaet )
print(file.writable())

file.write('Hello Anvar\n') # esli byly dannye , to oni udalyautsaya i zapisuvayetsya  novue
file.write('bootcapm\n')

file.writelines(['Hello\n', 'Anvar\n'])

file.close()

'------------------------------Append------------------------------'

file = open('new_file.txt', 'a')
file.write('Mew Line')
file.seek(0)
file.write('start') # vsr ravno zapishet v konce



file.close()



'==================Kontekstnyi menedger=================='

# konstrukciya with

# try:
#     file = open ('sdffgh', 'w')
#     file.read()
# finally:
#     file.close()


with open('test.txt', 'r') as file:
    print(file.read())

print(file.closed) #True - fail zskrylsy 

try:
    file = open('test.txt', 'r')
    print(file.read())

finally:
    file.close()

    # konstrukciya with rabotaet s lubymi obyektami u kotoryh est 2 metoda _enter_, _exit_
    #_enter_ - rabotaet nachale konstrukcii with
    # _exit_ - rabotaet kogda konstrukciya zakonhila raboty ili vyshla oshibka v etoi konstrukcii (finally)
    