import led_matrix.glyphs.alpha_num as alpha_num

class Glyph:
    # data == [{"x", "y", "on"}]
    def __init__(self, data, width, height):
        self.__data = data
        self.width = width
        self.height = height


    def __iter__(self):
        return iter(self.__data)


    @classmethod
    def strlen(self, msg:str, spacing=0):
        """ Return length of the msg/str in LEDs """
        # Assumes mono-spaced "font"
        glyph = Glyph.get(msg[0])
        length = len(msg) * (glyph.width + spacing)
        # length = (glyph.width * len(msg)) + (len(msg)-1 * spacing)
        return length


    @classmethod
    def get(cls, name):
        glyph_set = None
        glyph_name = str(name).upper()

        if glyph_name in alpha_num.DATA.keys():
            glyph_set = alpha_num
        else:
            raise ValueError(f"Unknown Glyph: '{name}'")

        glyph_data = cls.__get_data(
            glyph_set.TEMPLATE,
            glyph_set.DATA.get(glyph_name)
        )
        glyph = Glyph(glyph_data, width=glyph_set.WIDTH, height=glyph_set.HEIGHT)

        return glyph


    @classmethod
    def __get_data(cls, template, pixels):
        data = []
        for idx, loc in enumerate(template):
            px_data = {
                "x": loc[1],
                "y": loc[0],
                "on":  True if pixels[idx] == 1 else False
            }

            data.append(px_data)

        return data
