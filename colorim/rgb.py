class Rgb:
    END = "\x1b[0m"

    @classmethod
    def rgb(cls, r, g, b, text):
        esc_string = f"\033[38;2;{r};{g};{b}m"
        output = esc_string + text + cls.END
        return output