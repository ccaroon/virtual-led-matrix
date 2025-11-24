import pygame

from abc import ABC, abstractmethod

from pixel_matrix.pixel_matrix import PixelMatrix

class Program(ABC):
    def __init__(self, **kwargs):
        self.__matrix = PixelMatrix(**kwargs)


    @property
    def matrix(self):
        return self.__matrix


    @abstractmethod
    def loop(self, pixel_matrix):
        """  Your PixelMatrix Program's main loop. """


    def execute(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.loop()

        self.matrix.quit()
