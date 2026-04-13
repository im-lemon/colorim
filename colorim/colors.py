class Color:
    RED_CODE = "\033[31;1m"
    GREEN_CODE = "\033[32;1m"
    BLUE_CODE = "\033[34;1m"
    PURPLE_CODE = "\033[38;2;179;0;254m"
    CHROME_YELLOW_CODE = "\033[38;2;255;171;0m"
    DIAMOND_CODE = "\033[38;2;204;202;251m"
    PINK_CODE = "\033[38;2;250;110;200m"
    HOT_PINK_CODE = "\033[38;2;255;180;170m"
    CYAN_CODE = "\033[36;1m"
    YELLOW_CODE = "\033[0;93m"
    LIGHT_YELLOW_CODE = "\033[1;93m"
    END = "\033[0m"

    @classmethod
    def red(cls, text):
        output=cls.RED_CODE+text+cls.END
        return output

    @classmethod
    def green(cls, text):
        output=cls.GREEN_CODE+text+cls.END
        return output

    @classmethod
    def blue(cls, text):
        output=cls.BLUE_CODE+text+cls.END
        return output

    @classmethod
    def purple(cls, text):
        output=cls.PURPLE_CODE+text+cls.END
        return output

    @classmethod
    def cyan(cls, text):
        output=cls.CYAN_CODE+text+cls.END
        return output

    @classmethod
    def yellow(cls, text):
        output=cls.YELLOW_CODE+text+cls.END
        return output

    @classmethod
    def light_yellow(cls, text):
        output=cls.LIGHT_YELLOW_CODE+text+cls.END
        return output
    @classmethod
    def chrome_yellow(cls, text):
        output=cls.CHROME_YELLOW_CODE+text+cls.END
        return output
    @classmethod
    def diamond(cls, text):
        output=cls.DIAMOND_CODE+text+cls.END
        return output
    @classmethod
    def pink(cls, text):
        output=cls.PINK_CODE+text+cls.END
        return output
    @classmethod
    def hot_pink(cls, text):
        output=cls.HOT_PINK_CODE+text+cls.END
        return output