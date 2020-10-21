import os
user1 = input("user1 name = ")
user2 = input("user2 name = ")
field = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
print("enter ships", user1)
a = [int(i) for i in input("first ship ").split()]
field[a[0] - 1][a[1] - 1] = 1
b = [int(i) for i in input("second ship ").split()]
field[b[0] - 1][b[1] - 1] = 1
c = [int(i) for i in input("third ship ").split()]
field[c[0] - 1][c[1] - 1] = 1
d = [int(i) for i in input("fourth ship ").split()]
field[d[0] - 1][d[1] - 1] = 1
os.system('cls')

field2 = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
print("enter ships", user2)
a = [int(i) for i in input("first ship ").split()]
field2[a[0] - 1][a[1] - 1] = 1
b = [int(i) for i in input("second ship ").split()]
field2[b[0] - 1][b[1] - 1] = 1
c = [int(i) for i in input("third ship ").split()]
field2[c[0] - 1][c[1] - 1] = 1
d = [int(i) for i in input("fourth ship ").split()]
field2[d[0] - 1][d[1] - 1] = 1
os.system('cls')

def shoot_first():
    shoot = input("shoot " + user1 + ": ").split()
    shoot = [int(s) for s in shoot]
    if field2[shoot[0] - 1][shoot[1] - 1] == 1:
        print("got")
        field2[shoot[0] - 1][shoot[1] - 1] = 0
        return True
    else:
        print("not got")
        return False

def shoot_second():
    shoot = input("shoot " + user2 + ": ").split()
    shoot = [int(s) for s in shoot]
    if field[shoot[0] - 1][shoot[1] - 1] == 1:
        print("got")
        field[shoot[0] - 1][shoot[1] - 1] = 0
        return True
    else:
        print("not got")
        return False

def check():
    if sum([sum(f) for f in field2]) == 0:
        print("win", user1)
        return False
    if sum([sum(f) for f in field]) == 0:
        print("win", user2)
        return False
    return True

finish = True
while True:
    got = True
    while got:
        got = shoot_first()
        finish = check()
        if finish == False:
            break

    if finish == False:
        break
    got = True
    while got:
        got = shoot_second()
        finish = check()
        if finish == False:
            break