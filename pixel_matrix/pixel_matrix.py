import pygame

class PixelMatrix:
    DEFAULT_WIDTH = 1280
    DEFAULT_HEIGHT = 720

    PIXEL_SHAPE_SQUARE = "square"
    PIXEL_SHAPE_CIRCLE = "circle"
    VALID_PIXEL_SHAPES = (
        PIXEL_SHAPE_CIRCLE,
        PIXEL_SHAPE_SQUARE
    )

    def __init__(self, **kwargs):
        """
        Simulate a physical LED Matrix with Pixels.

        The Pixel Matrix's origin is at the top-left (0,0). The bottom-right
        is located at (width, height).


        => virtual-led-matrix


        Args:
            N/A

        KWArgs:
            width (int): Width of matrix in pixels
            height (int): Height of matrix in pixels
            title (str): Title for the Pixel Matrix Window
            pixel_size (int): The size of each pixel. Default: 1
            pizel_spacing (int): The spacing between pixels. Default: 0
            pixel_shape (str): PIXEL_SHAPE_(SQUARE|CIRCLE). Default: SQUARE

        NOTE: Pixel Size == 1 for any shape pixel => Single screen pixel
        """
        pygame.init()

        self.__pixel_size = kwargs.pop("pixel_size", 1)
        self.__pixel_shape = kwargs.pop("pixel_shape", self.PIXEL_SHAPE_SQUARE).lower()
        self.__pixel_spacing = kwargs.pop("pixel_spacing", 0)

        self.__width = kwargs.pop("width", self.DEFAULT_WIDTH)
        self.__height = kwargs.pop("height", self.DEFAULT_HEIGHT)

        surface_width = (self.__width * self.__pixel_size) + (self.__pixel_spacing * (self.__width - 1))
        surface_height = (self.__height * self.__pixel_size) + (self.__pixel_spacing * (self.__height - 1))

        title = kwargs.pop("title", f"Pixel Matrix ({self.width},{self.height})")
        if title:
            pygame.display.set_caption(title)


        print(f"Surface ({surface_width}x{surface_height})")
        print(f"Pixel ({self.width},{self.height})")
        self.__surface = pygame.display.set_mode(
            (surface_width, surface_height)
        )


    @property
    def width(self):
        """ Pixel Matrix's width in Pixels """
        return self.__width


    @property
    def height(self):
        """ Pixel Matrix's height in Pixels """
        return self.__height


    def set_background(self, color):
        """
        Set the background color

        NOTE: Does not turn on each pixel
        """
        self.__surface.fill(color)


    def set_pixel(self, px, py, color):
        if self.__pixel_size > 1:
            match self.__pixel_shape:
                case self.PIXEL_SHAPE_CIRCLE:
                    offset = self.__pixel_size / 2

                    cx = (px * self.__pixel_size) + offset + (px * self.__pixel_spacing)
                    cy = (py * self.__pixel_size) + offset + (py * self.__pixel_spacing)

                    pygame.draw.circle(
                        self.__surface, color,
                        (cx, cy), self.__pixel_size / 2
                    )
                case self.PIXEL_SHAPE_SQUARE:
                    rx = (px * self.__pixel_size) + (px * self.__pixel_spacing)
                    ry = (py * self.__pixel_size) + (py * self.__pixel_spacing)

                    pygame.draw.rect(
                        self.__surface, color,
                        pygame.Rect(rx, ry,
                            self.__pixel_size, self.__pixel_size
                        )
                    )
                case _:
                    raise ValueError(f"Unsupported value for pixel_shape: [{self.__pixel_shape}]")
        else:
            x = px + (px * self.__pixel_spacing)
            y = py + (py * self.__pixel_spacing)
            self.__surface.set_at((x, y), color)


    def update(self):
        pygame.display.flip()


    def quit(self):
        pygame.quit()






#
