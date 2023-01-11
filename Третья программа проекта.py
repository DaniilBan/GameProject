import json
from operator import itemgetter
with open('SpisokIgrokov2', 'r') as j:
    SpisokIgrokov = json.load(j)
Turnumbertwo = len(SpisokIgrokov) // 2
print(SpisokIgrokov)
a = 0
c = 0
b = c + 1
while a != Turnumbertwo:
    if SpisokIgrokov[c][6] == SpisokIgrokov[b][1]:
        results = input("Напишите игрока,который выиграл или в случае ничьи напишите 'ничья'")
        if results == SpisokIgrokov[c][1]:
           SpisokIgrokov[c][5] = SpisokIgrokov[c][5] + 1
        elif results == SpisokIgrokov[b][1]:
            SpisokIgrokov[b][5] = SpisokIgrokov[b][5] + 1
        elif results == 'ничья':
            SpisokIgrokov[c][5] = SpisokIgrokov[c][5] + 0,5
            SpisokIgrokov[b][5] = SpisokIgrokov[b][5] + 0,5
        else:
            print('Неверный ввод результата, срочно прекратите работу программы')
        c = b + 1
        b += 2
        a += 1
    elif SpisokIgrokov[c][6] == SpisokIgrokov[b + 1][1]:
        results = input("Напишите игрока,который выиграл или в случае ничьи напишите 'ничья'")
        b += 1
        if results == SpisokIgrokov[c][1]:
           SpisokIgrokov[c][5] = SpisokIgrokov[c][5] + 1
        elif results == SpisokIgrokov[b][1]:
            SpisokIgrokov[b][5] = SpisokIgrokov[b][5] + 1
        elif results == 'ничья':
            SpisokIgrokov[c][5] = SpisokIgrokov[c][5] + 0,5
            SpisokIgrokov[b][5] = SpisokIgrokov[b][5] + 0,5
        else:
            print('Неверный ввод результата, срочно прекратите работу программы')
        c += 1
        b += 1
        a += 1
if len(SpisokIgrokov) % 2 != 0:
    SpisokIgrokov[-1][5] += 1
SpisokIgrokov = sorted(SpisokIgrokov,key = itemgetter(5),reverse = True)
for i in range(len (SpisokIgrokov)):
    print(SpisokIgrokov[i])
