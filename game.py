import numpy as np
import os
import noise

pycharm = input("pycharm? y/n ")
if pycharm == "y":
    pycharm = True
elif pycharm == "n":
    pycharm = False

def clear():
    pycharm = True
    if pycharm == True:
        print('\n' * 80)
    elif pycharm != True:
        os.system('cls' if os.name == 'nt' else 'clear')


stopped = False
shape = (250, 250)
playing_field = np.zeros(shape=(250, 250), dtype="<U100")
x = 45
y = 105

def fill(pf):
    y = 0
    x = 0
    while y < 250:
        while x < 250:

            r = noise.snoise2(x, y, octaves=5, persistence=1.5, lacunarity=0.5, repeatx=250, repeaty=250, base=16)
            pf[y][x] = r
            x = x + 1
        x = 0
        y = y + 1


def edit(pf):
    y = 0
    x = 0
    while y < 250:
        while x < 250:
            if pf[y][x] > "0.3":
                pf[y][x] = "3"
            elif pf[y][x] >= "-0.07":
                pf[y][x] = "2"
            else:
                pf[y][x] = "1"
            x = x + 1
        x = 0
        y = y + 1


def fancy(pf):
    y = 0
    x = 0
    while y < 250:
        while x < 250:

            if pf[y][x] == "1":
                pf[y][x] = "\u001b[34mO\033[30m"
            elif pf[y][x] == "2":
                pf[y][x] = "\u001b[32mF\033[30m"
            elif pf[y][x] == "3":
                pf[y][x] = "\u001b[37mX\033[30m"
            x = x + 1
        x = 0
        y = y + 1


def render(pf, x, y):
    w = y
    z = x
    while y < w+41:

        while x < z + 161:
            print((y+w)/2)
            print((x+z)/2)
            if pf[y][x] == pf[(y+w)/2][(x+z)/2]:
                pf[y][x] = "\u001b[91mikwildood\033[30m"
                print(pf[y][x], end="", flush=True)
            else:
                print(pf.item(x, y), end="", flush=True)
            x = x + 1
        y = y + 1
        x = z
        print()


fill(playing_field)
edit(playing_field)
fancy(playing_field)
render(playing_field, x, y)


def move(x, y):
    stop = False
    z = input()
    if z == "up":
        y = y+1
    elif z == "down":
        y = y-1
    elif z == "right":
        x = x+1
    elif z == "left":
        x = x-1
    elif z == "stop":
        stop = True
    clear()
    render(playing_field, x, y)
    return x, y, stop


while stopped == False:
    x, y, stopped = move(x, y)
    if stopped:
        clear()


