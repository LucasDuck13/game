import random
import numpy as np
# import os

shape = (250, 250)
playing_field = np.zeros(shape=(250, 250), dtype="<U100")


def fill(pf):
    y = 0
    x = 0
    while y < 250:
        while x < 250:

            r = random.randint(1, 3)
            pf[y][x] = r
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
    while y < w+10:
        print(pf.item(x, y)+pf.item(x+1, y)+pf.item(x+2, y)+pf.item(x+3, y)+pf.item(x+4, y)+pf.item(x+5, y) +
              pf.item(x+6, y)+pf.item(x+7, y)+pf.item(x+8, y)+pf.item(x+9, y)+pf.item(x+10, y)+pf.item(x+11, y) +
              pf.item(x+12, y)+pf.item(x+13, y)+pf.item(x+14, y)+pf.item(x+15, y)+pf.item(x+16, y) +
              pf.item(x+17, y)+pf.item(x+18, y)+pf.item(x+19, y))
        y = y + 1


fill(playing_field)
fancy(playing_field)
render(playing_field, 125, 125)
