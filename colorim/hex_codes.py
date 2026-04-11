from .rgb import Rgb
class Hex:
    @classmethod
    def hex(cls, hex_code, text):
        hex_code = hex_code.lstrip('#').lower()
        if len(hex_code) != 6:
            raise ValueError('Invalid hex code')

        r=hex_code[0:2]
        g=hex_code[2:4]
        b=hex_code[4:6]
        r=int(r,16)
        g=int(g,16)
        b=int(b,16)
        return Rgb.rgb(r,g,b, text=text)