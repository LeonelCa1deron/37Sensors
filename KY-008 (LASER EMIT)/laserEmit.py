# Dueñas Nuñez Alan Gabriel 19211630
# Código para sensor KY-008 (LASER EMIT)

import time
from machine import Pin

laser = Pin(26, Pin.OUT)

while True:
    
    print("Laser Encendido")
    laser.on()  
    time.sleep(2)
    
    print("Laser Apagado")
    laser.off()    
    time.sleep(2)