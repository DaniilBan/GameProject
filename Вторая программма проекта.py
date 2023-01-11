import json
from operator import itemgetter
with open('Spisokigrokov', 'r') as j:
    SpisokIgrokov = json.load(j)
with open('Tur','r') as i:
    Turnumberone = json.load(i)
a = 0
c = 0
b = c + 1
d = len(SpisokIgrokov)
if d % 2 == 0:
    while a != len(Turnumberone):
        results = str(input('Введите результат: 1-0,если выиграли белые,0-1,если чёрные и 0,5-0,5,если ничья'))
        if results == '1-0':
            SpisokIgrokov[c].append(1)
            SpisokIgrokov[b].append(0)
            a += 1
        elif results == '0-1':
            SpisokIgrokov[c].append(0)
            SpisokIgrokov[b].append(1)
            a += 1
        elif results == '0,5-0,5':
            SpisokIgrokov[c].append(0.5)
            SpisokIgrokov[b].append(0.5)
            a += 1
        else:
            print('Неверный ввод результата, повторите попытку!')
        c += 2
        b += 2
else:
    while a != len(Turnumberone) - 1:
        results = str(input('Введите результат: 1-0,если выиграли белые,0-1,если чёрные и 0,5-0,5,если ничья'))
        if results == '1-0':
            SpisokIgrokov[c].append(1)
            SpisokIgrokov[b].append(0)
            a += 1
        elif results == '0-1':
            SpisokIgrokov[c].append(0)
            SpisokIgrokov[b].append(1)
            a += 1
        elif results == '0,5-0,5':
            SpisokIgrokov[c].append(0.5)
            SpisokIgrokov[b].append(0.5)
            a += 1
        else:
            print('Неверный ввод результата, повторите попытку!')
        c += 2
        b += 2
    SpisokIgrokov[-1].append(1)
SpisokIgrokov = sorted(SpisokIgrokov,key = itemgetter(5),reverse = True)
f = 0
g = f + 1
h = len(SpisokIgrokov)
if h % 2 == 0:
    while f != h:
        if SpisokIgrokov[f][1] == SpisokIgrokov[g][4]:
            g += 1
            if SpisokIgrokov[f][3] > SpisokIgrokov[g][3] or SpisokIgrokov[f][3] == SpisokIgrokov[g][3] and SpisokIgrokov[f][2] < SpisokIgrokov[g][2]:
                print(SpisokIgrokov[f][1] + ' - ' + SpisokIgrokov[g][1])
                SpisokIgrokov[f].append(SpisokIgrokov[g][1])
                SpisokIgrokov[g].append(SpisokIgrokov[f][1])
                f += 1
                g += 1
            else:
                print(SpisokIgrokov[g][1] + ' - ' + SpisokIgrokov[f][1])
                SpisokIgrokov[f].append(SpisokIgrokov[g][1])
                SpisokIgrokov[g].append(SpisokIgrokov[f][1])
                f += 1
                g += 1 
        else:
            if SpisokIgrokov[f][3] > SpisokIgrokov[g][3] or SpisokIgrokov[f][3] == SpisokIgrokov[g][3] and SpisokIgrokov[f][2] < SpisokIgrokov[g][2]:
                print(SpisokIgrokov[f][1] + ' - ' + SpisokIgrokov[g][1])
                SpisokIgrokov[f].append(SpisokIgrokov[g][1])
                SpisokIgrokov[f].append(0)
                SpisokIgrokov[g].append(SpisokIgrokov[f][1])
                SpisokIgrokov[g].append(1)
                f = g + 1
                g += 2
            else:
                print(SpisokIgrokov[g][1] + ' - ' + SpisokIgrokov[f][1])
                SpisokIgrokov[f].append(SpisokIgrokov[g][1])
                SpisokIgrokov[g].append(SpisokIgrokov[f][1])
                SpisokIgrokov[f].append(1)
                SpisokIgrokov[g].append(0)
                f = g + 1
                g += 2
else:
    while f != h - 1:
        if SpisokIgrokov[f][1] == SpisokIgrokov[g][4]:
            g += 1
            if SpisokIgrokov[f][3] > SpisokIgrokov[g][3] or SpisokIgrokov[f][3] == SpisokIgrokov[g][3] and SpisokIgrokov[f][2] < SpisokIgrokov[g][2]:
                print(SpisokIgrokov[f][1] + ' - ' + SpisokIgrokov[g][1])
                SpisokIgrokov[f].append(SpisokIgrokov[g][1])
                SpisokIgrokov[g].append(SpisokIgrokov[f][1])
                f += 1
                g += 1
            else:
                print(SpisokIgrokov[g][1] + ' - ' + SpisokIgrokov[f][1])
                SpisokIgrokov[f].append(SpisokIgrokov[g][1])
                SpisokIgrokov[g].append(SpisokIgrokov[f][1])
                f += 1
                g += 1 
        else:
            if SpisokIgrokov[f][3] > SpisokIgrokov[g][3] or SpisokIgrokov[f][3] == SpisokIgrokov[g][3] and SpisokIgrokov[f][2] < SpisokIgrokov[g][2]:
                print(SpisokIgrokov[f][1] + ' - ' + SpisokIgrokov[g][1])
                SpisokIgrokov[f].append(SpisokIgrokov[g][1])
                SpisokIgrokov[f].append(0)
                SpisokIgrokov[g].append(SpisokIgrokov[f][1])
                SpisokIgrokov[g].append(1)
                f = g + 1
                g += 2
            else:
                print(SpisokIgrokov[g][1] + ' - ' + SpisokIgrokov[f][1])
                SpisokIgrokov[f].append(SpisokIgrokov[g][1])
                SpisokIgrokov[g].append(SpisokIgrokov[f][1])
                SpisokIgrokov[f].append(1)
                SpisokIgrokov[g].append(0)
                f = g + 1
                g += 2 
    print(SpisokIgrokov[-1][1] + ' - ' + 'bye')
    SpisokIgrokov[-1].append('bye')
    SpisokIgrokov[-1].append(0)
for i in range(len (SpisokIgrokov)):
    print(SpisokIgrokov[i])
with open('SpisokIgrokov2','w') as file:
    json.dump(SpisokIgrokov,file)    

