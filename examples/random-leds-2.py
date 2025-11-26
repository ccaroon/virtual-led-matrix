#!/usr/bin/env python
from led_matrix.color import Color
from led_matrix.program import Program

import random

def random_leds(matrix):
    """
    Turn on random LEDs in random colors.

    The program will continue to run until the window is closed.

    Args:
        matrix (LEDMatrix): The LEDMatrix to be controlled. Automatically
                            created by Program.
    """
    x = random.randint(0, matrix.width)
    y = random.randint(0, matrix.height)

    color = Color.random()

    matrix.set_led(x, y, color)
    matrix.update()


Program.exec_func(
    # The function to use as the event loop
    random_leds,
    # Params that are passed to the LEDMatrix constructor
    width=1024, height=1024,
    title="Random LEDs #2"
)
