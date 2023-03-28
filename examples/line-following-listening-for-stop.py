from microbit import *
import radio
radio.on()

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

'''
This tells us which of the micro:bit's pins is connected to which input on the motor driver (follow the coloured wires!).
e.g. FL means that it controls the pin that turns on the left-hand motor in the forward direction.
'''
FL = pin13
BL = pin12
FR = pin15
BR = pin14

'''
If the pin is set to LOW (0), the motor is turned off. The lower the number, the faster the motor goes.
Currently the motors are set to turn on at half speed (511), as this makes it easier to control.
'''
on = 500
off = 0

'''
The following functions define the combination of pins to control direction.
'''
def stop(time=100):
    display.clear()
    FL.write_analog(off)
    BL.write_analog(off)
    FR.write_analog(off)
    BR.write_analog(off)
    sleep(time)

def forward(time, speed=on):
    display.show(Image.ARROW_N)
    FL.write_analog(speed)
    BL.write_analog(off)
    FR.write_analog(speed)
    BR.write_analog(off)
    sleep(time)
    stop()

def backward(time, speed=on):
    display.show(Image.ARROW_S)
    FL.write_analog(off)
    BL.write_analog(speed)
    FR.write_analog(off)
    BR.write_analog(speed)
    sleep(time)
    stop()

def left_turn(time, speed=on):
    display.show(Image.ARROW_W)
    FL.write_analog(off)
    BL.write_analog(speed)
    FR.write_analog(speed)
    BR.write_analog(off)
    sleep(time)
    stop()

def right_turn(time, speed=on):
    display.show(Image.ARROW_E)
    FL.write_analog(speed)
    BL.write_analog(off)
    FR.write_analog(off)
    BR.write_analog(speed)
    sleep(time)
    stop()

stop()

while True:
    message = radio.receive()

    while message is not "stop":
        message = radio.receive()

        left_sensor = pin2.read_analog()
        right_sensor = pin1.read_analog()
        print("left = " + str(left_sensor) + "; right = " + str(right_sensor))

        if left_sensor <= 100 and right_sensor <= 100:
            display.show(Image.ARROW_N)
            forward(100)
        elif left_sensor > 100:
            display.show(Image.ARROW_W)
            left_turn(100)
        elif right_sensor > 100:
            display.show(Image.ARROW_E)
            right_turn(100)
        sleep(100)
    stop()
