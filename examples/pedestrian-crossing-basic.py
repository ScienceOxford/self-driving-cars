# Imports go at the top
from microbit import *
import radio
radio.config(channel=7)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        for x in range(5000):
            radio.send("stop")
            sleep(1)
        sleep(1000)
    else:
        radio.send("go")
        sleep(1)