#!/usr/bin/env python
import argparse
import pygame
import time

from pixel_matrix.color import Color
from pixel_matrix.pixel_matrix import PixelMatrix
from pixel_matrix.program import Program

class PixelWalker(Program):
    def __init__(self, **kwargs):
        # PixelMatrix options are removed from kwargs when super().__init__()
        # is called.
        super().__init__(**kwargs)

        # Variables/state relevant to our program
        self.__x = 0
        self.__y = 0
        self.__color = Color.make(kwargs.get("color", "green"))
        self.__delay = kwargs.get("delay", 0.025)


    def loop(self):
        if self.__x < self.matrix.width and self.__y < self.matrix.height:
            self.matrix.set_pixel(self.__x, self.__y, self.__color)

            self.__x += 1

            if self.__x >= self.matrix.width:
                self.__x = 0
                self.__y += 1

            self.matrix.update()
            time.sleep(self.__delay)
        else:
            print("Sequence Complete! Close the window to exit.")
            self.wait_for(pygame.MOUSEBUTTONDOWN)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pixel Walker")

    parser.add_argument("--width", "-w",
        type=int, default=64, help="Pixel Matrix Width")
    parser.add_argument("--height", "-g",
        type=int, default=64, help="Pixel Matrix Height")
    parser.add_argument("--size", "-s",
        type=int, default=10, help="Pixel Size")
    parser.add_argument("--spacing", "-p",
        type=int, default=1, help="Space between pixels")
    parser.add_argument("--delay", "-d",
        type=float, default=0.025, help="Delay between drawing each pixel")
    parser.add_argument("--shape", "-a",
        choices=(PixelMatrix.VALID_PIXEL_SHAPES),
        default=PixelMatrix.PIXEL_SHAPE_SQUARE, help="Pixel Shape")
    parser.add_argument("--color", "-c",
        type=str, default="green", help="Color of each pixel: 'red', '0xffffff', '#00ffff', etc")

    args = parser.parse_args()

    program = PixelWalker(
        title = "Pixel Walker",
        width = args.width, height = args.height,
        pixel_size = args.size,
        pixel_spacing = args.spacing,
        pixel_shape=args.shape,
        color=args.color,
        delay=args.delay
    )
    program.execute()





#
