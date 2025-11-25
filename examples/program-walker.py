#!/usr/bin/env python
import pygame
import time

from pixel_matrix.color import Color
from pixel_matrix.program import Program

class PixelWalker(Program):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__x = 0
        self.__y = 0
        self.__color = Color.make("green")


    def on_mouse_down(self, position):
        print(position)


    def loop(self):
        if self.__x < self.matrix.width and self.__y < self.matrix.height:
            self.matrix.set_pixel(self.__x, self.__y, self.__color)

            self.__x += 1

            if self.__x >= self.matrix.width:
                self.__x = 0
                self.__y += 1

            self.matrix.update()
            # time.sleep(0.025)
            self.wait_for(pygame.MOUSEBUTTONDOWN)
        else:
            print("Sequence Complete!")
            self.wait_for(pygame.MOUSEBUTTONDOWN)


if __name__ == "__main__":
    program = PixelWalker(
        title = "Pixel Walker",
        width = 16, height = 5,
        pixel_size = 50,
        pixel_spacing = 5,
        pixel_shape="circle"
    )
    program.execute()
