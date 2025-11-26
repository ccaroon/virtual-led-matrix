#!/usr/bin/env python
from pixel_matrix.color import Color
from pixel_matrix.program import Program

import random

def random_dots(matrix):
    """
    Display randomly placed dots (pixels) in random colors.

    The program will continue to run until the window is closed.

    Args:
        matrix (PixelMatrix): The Pixel Matrix to be controlled.
    """
    x = random.randint(0, matrix.width)
    y = random.randint(0, matrix.height)

    color = Color.random()

    matrix.set_pixel(x, y, color)
    matrix.update()


Program.exec_func(
    # The function to use as the event loop
    random_dots,
    # Params that are passed to the PixelMatrix constructor
    width=1024, height=1024,
    title="Random Dots"
)
