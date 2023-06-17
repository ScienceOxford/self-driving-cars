# Imports go at the top
from microbit import *
import radio
radio.config(channel=7)
radio.on()

'''
Change the number below to match your car's number
'''
car_channel = 21

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        for x in range(2000):
            radio.send("stop")
            radio.config(channel=car_channel)
            radio.send("stop")
            radio.config(channel=7)
            sleep(1)
        #sleep(1000)
    else:
        radio.send("go")
        radio.config(channel=car_channel)
        radio.send("go")
        radio.config(channel=7)
        sleep(1)