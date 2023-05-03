# this is a simple program to blink the onboard led of the raspberry pi pico

from machine import Pin
import time

led = Pin(25, Pin.OUT)

while True:
    led.value(1)
    time.sleep(1)

