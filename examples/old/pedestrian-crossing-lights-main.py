# Imports go at the top
from microbit import *
import radio
radio.config(channel=7)
radio.on()

red = pin0
amber = pin1
green = pin2

red.write_digital(1)
# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        for x in range(2000):
            radio.send("stop")
            sleep(1)
        red.write_digital(0)
        green.write_digital(1)
        for x in range(3000):
            radio.send("stop")
            sleep(1)
        green.write_digital(0)
        red.write_digital(1)
        sleep(1000)
    else:
        radio.send("go")
        sleep(1)