import json
from operator import itemgetter
Spisok = dict()
n_people = int(input('Введите колличество игроков'))
a = 0
c = 0
for i in range(n_people):
    Players = input('Введите имя игрока')
    ELO = int(input('Введите международный рейтинг игрока'))
    ROS = int(input('Введите российский рейтинг игрока'))
    middle = (ROS + ELO) / 2
    Spisok[middle] = Players
SpisokIgrokov = sorted(Spisok.items(),reverse = True)
print(SpisokIgrokov)
a = 'ч'
d = len(SpisokIgrokov)
b = c + 1
x = 'bye'
Numbertable = 1
Turnumberone = []
if d % 2 == 0:
    while c != d:
        print(f"{Numbertable}. {c + 1}({SpisokIgrokov[c][1]}) - {b + 1}({SpisokIgrokov[b][1]})")
        SpisokIgrokov[c] = SpisokIgrokov[c] + (c + 1,) + (0,) + (SpisokIgrokov[b][1],)
        SpisokIgrokov[b] = SpisokIgrokov[b] + (b + 1,) + (1,) + (SpisokIgrokov[c][1],)
        Turnumberone.append(f"{SpisokIgrokov[c][1]} - {SpisokIgrokov[b][1]}")
        c += 2
        b += 2
        Numbertable += 1
else:
    while c != d - 1:
        print(f"{Numbertable}. {c + 1}({SpisokIgrokov[c][1]}) - {b + 1}({SpisokIgrokov[b][1]})")
        Turnumberone.append(f"{SpisokIgrokov[c][1]} - {SpisokIgrokov[b][1]}")
        SpisokIgrokov[c] = SpisokIgrokov[c] + (c + 1,) + (0,) + (SpisokIgrokov[b][1],)
        SpisokIgrokov[b] = SpisokIgrokov[b] + (b + 1,) + (1,) + (SpisokIgrokov[c][1],)
        c += 2
        b += 2
        Numbertable += 1
if d % 2 == 0:
    print(Turnumberone)
    print(SpisokIgrokov)
else:
    SpisokIgrokov[c] = SpisokIgrokov[c] + (c + 1,) + (0,) + ('bye',)
    Turnumberone.append(SpisokIgrokov[c][1] + ' - ' + x)
    print(SpisokIgrokov[c][1] + '-' + x)
    print(Turnumberone)
    print(SpisokIgrokov)


def result():
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


result()
SpisokIgrokov = sorted(SpisokIgrokov, key=itemgetter(5), reverse=True)
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
with open('SpisokIgrokov2', 'w') as file:
    json.dump(SpisokIgrokov, file)