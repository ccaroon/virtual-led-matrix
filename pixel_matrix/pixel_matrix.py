import pygame

class PixelMatrix:
    PIXEL_SHAPE_SQUARE = "square"
    PIXEL_SHAPE_CIRCLE = "circle"

    def __init__(self, width, height, **kwargs):
        """
        Args:
            width (int): Width of matrix
            height (int): Height of matrix

        KWArgs:
            pixel_size (int): The size of each pixel. Default: 1
            pitch (int): The spacing between pixels. Default: 0
            pixel_shape (str): PIXEL_SHAPE_(SQUARE|CIRCLE). Default: SQUARE

        NOTE: Pixel Size == 1 for any shape pixel => Single Dot
        """
        pygame.init()
        title = kwargs.get("title")
        if title:
            pygame.display.set_caption(title)

        px_size = kwargs.get("pixel_size", 1)
        px_shape = kwargs.get("pixel_shape", self.PIXEL_SHAPE_SQUARE)
        pitch = kwargs.get("pitch", 0)

        # TODO: calc based on size, spacing, etc
        self.__surface = pygame.display.set_mode((width, height))


    def set_background(self, color):
        self.__surface.fill(color)


    def set_pixel(self, x, y, color):
        self.__surface.set_at((x, y), color)


    def update(self):
        pygame.display.flip()


    @classmethod
    def run(cls, program, **kwargs):
        # TODO Create PM Instance
        matrix = PixelMatrix(1024, 1024, **kwargs)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # TODO: if `program` is a class, call Program.run()
            #       else if function, just call it
            program(matrix)

            # pygame.display.flip()

        pygame.quit()





#
