import json
END = 1
Players = input('Введите имя игрока')
ELO = int(input('Введите международный рейтинг игрока'))
ROS = int(input('Введите российский рейтинг игрока'))
Spisok = dict()
Средний = (ROS + ELO) / 2
a = 0
c = 0
while END != 0:
    Spisok[Средний] = Players
    Players = input('Введите имя игрока')
    ELO = int(input('Введите международный рейтинг игрока'))
    ROS = int(input('Введите российский рейтинг игрока'))
    Средний = (ROS + ELO) / 2
    END = int(input('Введите ноль,в следуюший раз,если игроки закончились'))
Spisok2 = sorted(Spisok.items(),reverse = True)
a = 'ч'
d = len(Spisok2)
b = c + 1
x = 'bye'
Numbertable = 1
Tur1 = list()
if d % 2 == 0:
    while c != d:
        print(str(Numbertable) + '. ' + str(c + 1) + '. ' + Spisok2[c][1] + ' - ' + Spisok2[b][1] + ' ' + str(b + 1))
        Spisok2[c] = Spisok2[c] + (c + 1,) + (0,) + (Spisok2[b][1],)
        Spisok2[b] = Spisok2[b] + (b + 1,) + (1,) + (Spisok2[c][1],)
        Tur1.append(Spisok2[c][1] + ' - ' + Spisok2[b][1])
        c += 2
        b += 2
        Numbertable += 1
else:
    while c != d - 1:
        print(str(Numbertable) + '. ' + str(c + 1) + '. ' + Spisok2[c][1] + ' - ' + Spisok2[b][1] + ' ' + str(b + 1))
        Tur1.append(Spisok2[c][1] + ' - ' + Spisok2[b][1])
        Spisok2[c] = Spisok2[c] + (c + 1,) + (0,) + (Spisok2[b][1],) 
        Spisok2[b] = Spisok2[b] + (b + 1,) + (1,) + (Spisok2[c][1],)
        c += 2
        b += 2
        Numbertable += 1
if d % 2 == 0:
    print(Tur1)
    print(Spisok2)
else:
    Spisok2[c] = Spisok2[c] + (c + 1,) + (0,) + ('bye',)
    Tur1.append(Spisok2[c][1] + ' - ' + x)
    print(Spisok2[c][1] + '-' + x)
    print(Tur1)
    print(Spisok2)
with open('Spisokigrokov', 'w') as file:
    json.dump(Spisok2, file)
with open('Tur', 'w') as file:
    json.dump(Tur1, file)
