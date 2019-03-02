import noise
#help(noise)
import numpy as np
from PIL import Image

D = np.zeros((250, 250), dtype=float)


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
            if pf[y][x] > 0.3333:
                pf[y][x] = 3
            elif pf[y][x] > -0.3333:
                pf[y][x] = 2
            elif pf[y][x] <= -0.3333:
                pf[y][x] = 1
            x = x + 1
        x = 0
        y = y + 1


fill(D)

print(D)
edit(D)

print(D)

