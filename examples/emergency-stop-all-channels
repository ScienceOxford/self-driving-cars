from microbit import *
import radio
radio.on()

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

running = False

while True:
    if button_a.was_pressed():
        running = "stop"
        display.show(Image.NO)
    if button_b.was_pressed():
        running = "go"
        display.show(Image.YES)
    for x in range(0, 84):
        radio.config(channel=x)
        radio.send(str(running))
        sleep(1)
