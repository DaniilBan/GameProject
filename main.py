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
SpisokIgrokov = sorted(Spisok.items(), reverse=True)
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

dopspis = []
for i in range(len(SpisokIgrokov)):
    dopspis.append(list(SpisokIgrokov[i]))
SpisokIgrokov = dopspis
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
                c += 2
                b += 2
            elif results == '0-1':
                SpisokIgrokov[c].append(0)
                SpisokIgrokov[b].append(1)
                a += 1
                c += 2
                b += 2
            elif results == '0,5-0,5':
                SpisokIgrokov[c].append(0.5)
                SpisokIgrokov[b].append(0.5)
                a += 1
                c += 2
                b += 2
            else:
                print('Неверный ввод результата, повторите попытку!')
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
SpisokIgrokovSave = []
def Result():
    newSpis = []
    if len(SpisokIgrokov) % 2 == 0:
        for i in range(len(SpisokIgrokov) // 2):
            results = str(input('Введите имя победителя. если ничья введите ничья'))
            for j in range(1, len(SpisokIgrokov)):
                if SpisokIgrokov[0][1] == SpisokIgrokov[j][-1]:
                    if SpisokIgrokov[0][1] == results:
                        SpisokIgrokov[0][5] += 1
                        newSpis.append(SpisokIgrokov[0])
                        newSpis.append(SpisokIgrokov[j])
                        del SpisokIgrokov[j]
                        del SpisokIgrokov[0]
                        break
                    elif SpisokIgrokov[j][1] == results:
                        SpisokIgrokov[j][5] += 1
                        newSpis.append(SpisokIgrokov[0])
                        newSpis.append(SpisokIgrokov[j])
                        del SpisokIgrokov[j]
                        del SpisokIgrokov[0]
                        break
                    else:
                        SpisokIgrokov[0][5] += 0.5
                        SpisokIgrokov[j][5] += 0.5
                        newSpis.append(SpisokIgrokov[0])
                        newSpis.append(SpisokIgrokov[j])
                        del SpisokIgrokov[j]
                        del SpisokIgrokov[0]
                        break
    else:
        for i in range(len(SpisokIgrokov)):
            if SpisokIgrokov[i][-1] == 'bye':
                SpisokIgrokov[i][5] += 1
                newSpis.append(SpisokIgrokov[i])
                del SpisokIgrokov[i]
                break
        for i in range(len(SpisokIgrokov) // 2):
            results = str(input('Введите имя победителя. если ничья введите ничья'))
            for j in range(1, len(SpisokIgrokov)):
                if SpisokIgrokov[0][1] == SpisokIgrokov[j][-1]:
                    if SpisokIgrokov[0][1] == results:
                        SpisokIgrokov[0][5] += 1
                        newSpis.append(SpisokIgrokov[0])
                        newSpis.append(SpisokIgrokov[j])
                        del SpisokIgrokov[j]
                        del SpisokIgrokov[0]
                        break
                    elif SpisokIgrokov[j][1] == results:
                        SpisokIgrokov[j][5] += 1
                        newSpis.append(SpisokIgrokov[0])
                        newSpis.append(SpisokIgrokov[j])
                        del SpisokIgrokov[j]
                        del SpisokIgrokov[0]
                        break
                    else:
                        SpisokIgrokov[0][5] += 0.5
                        SpisokIgrokov[j][5] += 0.5
                        newSpis.append(SpisokIgrokov[0])
                        newSpis.append(SpisokIgrokov[j])
                        del SpisokIgrokov[j]
                        del SpisokIgrokov[0]
                        break
    return newSpis


def draw():
    otvet = []
    while len(SpisokIgrokov) % 2 != 0:
        if x in SpisokIgrokov[-1]:
            for i in range(-2, -len(SpisokIgrokov), -1):
                if SpisokIgrokov[i][1] not in SpisokIgrokov[-1]:
                    if SpisokIgrokov[i][3] >= SpisokIgrokov[-1][3] and SpisokIgrokov[i][2] < SpisokIgrokov[-1][2]:
                        otvet.append(f"{SpisokIgrokov[i][1]}-{SpisokIgrokov[-1][1]}")
                        SpisokIgrokov[-1][3] += 1
                        SpisokIgrokov[-1].append(SpisokIgrokov[i][1])
                        SpisokIgrokov[i].append(SpisokIgrokov[-1][1])
                    elif SpisokIgrokov[-1][3] >= SpisokIgrokov[i][3] and SpisokIgrokov[-1][2] < SpisokIgrokov[i][2]:
                        otvet.append(f"{SpisokIgrokov[-1][1]}-{SpisokIgrokov[i][1]}")
                        SpisokIgrokov[i][3] += 1
                        SpisokIgrokov[-1].append(SpisokIgrokov[i][1])
                        SpisokIgrokov[i].append(SpisokIgrokov[-1][1])
                    else:
                        otvet.append(f"{SpisokIgrokov[-1][1]}-{SpisokIgrokov[i][1]}")
                        SpisokIgrokov[-1][3] += 1
                        SpisokIgrokov[-1].append(SpisokIgrokov[i][1])
                        SpisokIgrokov[i].append(SpisokIgrokov[-1][1])
                    SpisokIgrokovSave.append(SpisokIgrokov[i])
                    SpisokIgrokovSave.append(SpisokIgrokov[-1])
                    print(SpisokIgrokovSave)
                    del SpisokIgrokov[i]
                    del SpisokIgrokov[-1]
                    break
        else:
            otvet.append(f"{SpisokIgrokov[-1][1]}-{x}")
            SpisokIgrokov[-1].append(x)
            SpisokIgrokovSave.append(SpisokIgrokov[-1])
            del SpisokIgrokov[-1]

    for w in range(len(SpisokIgrokov) // 2):
        print(w)
        for j in range(1, len(SpisokIgrokov)):
            if SpisokIgrokov[j][1] not in SpisokIgrokov[0]:
                if SpisokIgrokov[0][3] >= SpisokIgrokov[j][3] and SpisokIgrokov[0][2] < SpisokIgrokov[0][2]:
                    print(f"{SpisokIgrokov[0][1]}-{SpisokIgrokov[j][1]}")
                    SpisokIgrokov[j][3] += 1
                    SpisokIgrokov[j].append(SpisokIgrokov[0][1])
                    SpisokIgrokov[0].append(SpisokIgrokov[j][1])
                elif SpisokIgrokov[j][3] >= SpisokIgrokov[0][3] and SpisokIgrokov[j][2] < SpisokIgrokov[0][2]:
                    print(f"{SpisokIgrokov[j][1]}-{SpisokIgrokov[0][1]}")
                    SpisokIgrokov[j][3] += 1
                    SpisokIgrokov[j].append(SpisokIgrokov[0][1])
                    SpisokIgrokov[0].append(SpisokIgrokov[j][1])
                else:
                    print(1234)
                    print(f"{SpisokIgrokov[j][1]}-{SpisokIgrokov[0][1]}")
                    SpisokIgrokov[j][3] += 1
                    SpisokIgrokov[j].append(SpisokIgrokov[0][1])
                    SpisokIgrokov[0].append(SpisokIgrokov[j][1])
                SpisokIgrokovSave.append(SpisokIgrokov[j])
                SpisokIgrokovSave.append(SpisokIgrokov[0])
                print(SpisokIgrokovSave)
                del SpisokIgrokov[j]
                del SpisokIgrokov[0]
                break
    for k in otvet:
        print(k)

SpisokIgrokov.sort(key=lambda x:(-x[5], x[2]))

f = 0
g = f + 1
h = len(SpisokIgrokov)
draw()
SpisokIgrokovSave.sort(key=lambda x:(-x[5], x[2]))
SpisokIgrokov = SpisokIgrokovSave
print(SpisokIgrokov)
SpisokIgrokov = Result()
SpisokIgrokov.sort(key=lambda x:(-x[5], x[2]))
print(SpisokIgrokov)
for i in range(len (SpisokIgrokov)):
    print(SpisokIgrokov[i])
with open('SpisokIgrokov2', 'w') as file:
    json.dump(SpisokIgrokov, file)