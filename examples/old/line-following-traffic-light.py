from microbit import *
import radio
radio.on()

message = "stop"
display.show(Image.NO)

while True:
    if button_a.was_pressed():
        message = "go"
        display.show(Image.YES)
    elif button_b.was_pressed():
        message = "stop"
        display.show(Image.NO)
    radio.send(message)
    sleep(100)
