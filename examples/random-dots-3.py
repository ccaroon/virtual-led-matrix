#!/usr/bin/env python
from pixel_matrix.color import Color
from pixel_matrix.program import Program

import random

class RandomDots(Program):
    """
    A PixelMatrix Program that displays randomly placed dots (pixels) in random colors.

    Since it's defined as a class (sub-class of Program), it can keep track of
    state and other behavior beyond what you can do with the `Program.exec_func`
    style of writing a PixelMatrix program.

    KWArgs
        Accepts all kwargs that are used by the PixelMatrix class in addition to
        your own arguments need to initialize your Program. Arguments specific
        to PixelMatrix will be removed from the kwargs dict.
    """
    def __init__(self, **kwargs):
        # Remember to all super().__init__()
        super().__init__(**kwargs)


    # Automatically called by the event loop
    def loop(self):
        x = random.randint(0, self.matrix.width)
        y = random.randint(0, self.matrix.height)

        color = Color.random()

        self.matrix.set_pixel(x, y, color)
        self.matrix.update()


if __name__ == "__main__":
    program = RandomDots(
        title = "Random Dots",
        width = 1920, height = 1080
    )
    program.execute()
