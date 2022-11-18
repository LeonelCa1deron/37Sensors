from machine import Pin
import time

button = Pin(3, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 1:
        print("You pressed the button!")
    else:
        print("You loosen the button!")
    time.sleep(0.1)