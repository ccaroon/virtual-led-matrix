import pygame

class PixelMatrix:
    DEFAULT_WIDTH = 1280
    DEFAULT_HEIGHT = 720

    PIXEL_SHAPE_SQUARE = "square"
    PIXEL_SHAPE_CIRCLE = "circle"

    def __init__(self, **kwargs):
        """
        Args:

        KWArgs:
            width (int): Width of matrix
            height (int): Height of matrix
            title (str): Title for the Graphix Window
            pixel_size (int): The size of each pixel. Default: 1
            pitch (int): The spacing between pixels. Default: 0
            pixel_shape (str): PIXEL_SHAPE_(SQUARE|CIRCLE). Default: SQUARE

        NOTE: Pixel Size == 1 for any shape pixel => Single Dot
        """
        pygame.init()

        # TODO: calc based on size, spacing, etc
        self.__width = kwargs.pop("width", self.DEFAULT_WIDTH)
        self.__height = kwargs.pop("height", self.DEFAULT_HEIGHT)

        title = kwargs.pop("title", f"Pixel Matrix ({self.width},{self.height})")
        if title:
            pygame.display.set_caption(title)

        px_size = kwargs.pop("pixel_size", 1)
        px_shape = kwargs.pop("pixel_shape", self.PIXEL_SHAPE_SQUARE)
        pitch = kwargs.pop("pitch", 0)

        self.__surface = pygame.display.set_mode((self.width, self.height))


    @property
    def width(self):
        return self.__width


    @property
    def height(self):
        return self.__height


    def set_background(self, color):
        self.__surface.fill(color)


    def set_pixel(self, x, y, color):
        self.__surface.set_at((x, y), color)


    def line(self, start_pos, end_pos, color):
        pygame.draw.line(self.__surface, color, start_pos, end_pos)


    def update(self):
        pygame.display.flip()


    def quit(self):
        pygame.quit()






#
