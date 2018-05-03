class Mock_Adafruit_GPIO_SPI(object):
    def __init__(self):
        self.name = "Mock Adafruit GPIO SPI"

class Mock_Adafruit_GPIO(object):
    def __init__(self):
        self.name = "Mock Adafruit GPIO"
    SPI = Mock_Adafruit_GPIO_SPI

class Mock_Adafruit_SSD1306(object):