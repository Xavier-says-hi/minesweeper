import os
import random
import time
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
try:
    import keyboard
except:
    error = 1
    print("Run \"pip install keyboard\", or else this won't work.")
diffs = [[10, 10, 10], [16, 16, 40], [16, 30, 99], [20, 30, 130]]
colors = ['\x1b[5m0\x1b[0m', '\x1b[0;38;5;12m1\x1b[0m', '\x1b[0;38;5;2m2\x1b[0m', '\x1b[0;38;5;9m3\x1b[0m', '\x1b[0;38;5;4m4\x1b[0m', '\x1b[0;38;5;1m5\x1b[0m', '\x1b[0;38;5;6m6\x1b[0m', '\x1b[0;38;5;0m7\x1b[0m', '\x1b[0;38;5;8m8\x1b[0m']
def twodlist(a, b):
    c = [[[0 for _ in range(a)] for _ in range(b)] for _ in range(2)]
    return c
def calcelem(list0):
    k = 0
    for i in list0:
        for j in i:
            k = k + 1
    return [k, len(list0), len(i)]
def addmines(list0, num, x, y):
    if calcelem(list0[0])[0] > num + 9:
        for i in range(0, num):
            list0[0] = rollmine(list0[0], x, y)
        return list0
    else:
        return [["Error. Number of mines too big."]]
def render(list0):
    print("\x1b[0;38;5;12m1\x1b[0m")
    for i in list0:
        for j in i: #cursed images
            print(j, end=" ")
        print("\n")
def rollmine(list0, x, y):
    rx = random.randint(0, calcelem(list0)[2])
    ry = random.randint(0, calcelem(list0)[1])
    if (ry == y or ry == y + 1 or ry == y - 1) and (rx == x or rx == x + 1 or rx == x - 1) or list0[ry-1][rx-1] == 1: #first click safe, no mine stacking
        list0 = rollmine(list0, x, y)
    else:
        list0[ry-1][rx-1] = list0[ry-1][rx-1] + 1
    return list0
def compile(list0):
    for i in list0[0]:
        for j in i:
            if list0[1][i][j] == 1:
                pass
            else:
                print("", end=" ")
def gamestart(diff):
    

    map = diffs[diff]
clear()
for qwerty in range(len(colors)):
    print(colors[qwerty])
time.sleep(1000)
