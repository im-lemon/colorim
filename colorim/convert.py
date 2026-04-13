from .rgb import Rgb
class Convert:
    @classmethod
    def hex(cls, hex_code):
        hex = hex.lstrip('#')
        r = hex[0:2]
        g = hex[2:4]
        b = hex[4:6]
        r=int(r,16)
        g=int(g,16)
        b=int(b,16)
        return f"{hex} is {r} ,{g} ,{b} in RGB."

    @classmethod
    def rgb(cls, r,g,b):
        r=f"{r:02x}"
        g=f"{g:02x}"
        b=f"{b:02x}"
        conv_hex = "#" + r + g + b


        return f"Here's your hex code: {conv_hex}"