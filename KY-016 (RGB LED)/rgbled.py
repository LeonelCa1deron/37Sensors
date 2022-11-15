from machine import Pin
from time import sleep

btn = Pin(10,Pin.IN,Pin.PULL_UP)

while True:
    if btn.value()== 0:
        print(a)