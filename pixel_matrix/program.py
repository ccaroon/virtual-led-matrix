import pygame

from abc import ABC, abstractmethod

from pixel_matrix.pixel_matrix import PixelMatrix

class Program(ABC):
    def __init__(self, **kwargs):
        self.__matrix = PixelMatrix(**kwargs)


    @property
    def matrix(self):
        return self.__matrix


    def on_mouse_down(self, position):
        """ Event Handler for Mouse Down """
        pass


    def wait_for(self, event_type):
        while (event := pygame.event.wait()).type != event_type:
            if event.type == pygame.QUIT:
                pygame.quit()
                # pygame.event.post(
                #     pygame.event.Event(pygame.QUIT))
                # return


    @abstractmethod
    def loop(self, pixel_matrix):
        """  Your PixelMatrix Program's main loop. """


    def execute(self):
        """ Start the Program Running """
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.on_mouse_down(pos)

            self.loop()

        self.matrix.quit()


    @classmethod
    def exec_func(cls, program_func, **kwargs):
        """ Execute a function as a Pixel Matrix Program """
        class FuncProgram(Program):
            def loop(self):
                program_func(self.matrix)


        program = FuncProgram(**kwargs)
        program.execute()




#
