from .rgb import Rgb
class Convert:
    @classmethod
    def hex(cls, hex):
        hex = hex.lstrip('#')
        r = hex[0:2]
        g = hex[2:4]
        b = hex[4:6]
        r=int(r,16)
        g=int(g,16)
        b=int(b,16)
        return f"{hex} is {r},{g},{b} in RGB. It looks like this:\n"
        return Rgb.rgb(r,g,b, text="Hello world")