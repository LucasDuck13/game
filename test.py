import noise
import numpy as np

shape = (500, 500)
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

world = np.zeros(shape, dtype="<U100")
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i / scale,
                                    j / scale,
                                    octaves=octaves,
                                    persistence=persistence,
                                    lacunarity=lacunarity,
                                    repeatx=500,
                                    repeaty=500,
                                    base=0)


def add_color(world):
    color_world = np.zeros(world.shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if float(world[i][j]) < -0.05:
                color_world[i][j] = "1"
            elif float(world[i][j]) < 0.0:
                color_world[i][j] = "2"
            elif float(world[i][j]) < 1.0:
                (color_world[i][j]) = "3"

    return color_world


color_world = add_color(world)

print(color_world)
