from machine import Pin
import time

flame = Pin(0,Pin.IN)
    
while True:
    if flame.value() == 1:
        print("fuego!")
        time.sleep(1)
