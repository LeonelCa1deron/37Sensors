from machine import Pin
import time

BallSensor = Pin(17, Pin.IN)

while True:
    value = BallSensor.value()
    print(value, end = " ")
    if  value== 0:
        print("The ball is moving...")
    else:
        print("The ball isn't moving...")
    time.sleep(0.1)