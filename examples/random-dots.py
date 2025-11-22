#!/usr/bin/env python
from pixel_matrix.color import Color
from pixel_matrix.pixel_matrix import PixelMatrix

import random
# pm = PixelMatrix(1024, 1024)


def random_dots(matrix):
    x = random.randint(0, 1024)
    y = random.randint(0, 1024)

    green = Color.make("green")

    matrix.set_pixel(x, y, green)
    matrix.update()



PixelMatrix.run(random_dots, size=(1024,1024))
