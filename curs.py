import re

note = [7, 6, 8, 10, 5]

print("vechea lista",note)
note[0] = 9
note1 = note
print("noua lista",note1)

note[0] = note[4]
print("note inlocuite", note)

print(len(note))

#del(note[0])
#print(note)

suma = note[1] + note[2]
print(suma)

#inm = 3
#rez =[item * inm for item in note[0-5]]
#print(rez)


note = [7, 6, 8, 10, 5]
print(note[-1])

del(note[-2])
print("Lista modificata:", note)

note = [7, 6, 8, 10, 5]
print(note)

note.append(9)
print(note)

note.insert(0, 10)
print(note)

print("-----------------")

cifre = []
for i in range(10):
    cifre.insert(0, i + 1) #AICI SE PLEACA DE LA 0 DAR SE TOT ADUAGA NUMERELE CE CURGAND LA DREAPTA
print(cifre)

cifre = []
for i in range(10):
    cifre.append(i + 1) #AICI NUMERELE SE ADAUGA LA CAPAT
print(cifre)
