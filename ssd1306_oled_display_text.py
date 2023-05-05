# first install the ssd1306 micropython library in the lib folder 

from ssd1306 import SSD1306_I2C
from machine import Pin, I2C


WIDTH = 128
HIGHT = 64

i2c = I2C(0, scl = Pin(1), sda = Pin(0), freq = 400000)

display = SSD1306_I2C(WIDTH, HIGHT, i2c)

display.fill(0)
display.text("hello world", 0, 0)
display.show()
