from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from picozero import RGBLED
import utime
from oled import Write, GFX, SSD1306_I2C
from oled.fonts import ubuntu_mono_15, ubuntu_mono_20
import utime

WIDTH  = 128                                         
HEIGHT = 64
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000) 
rgb = RGBLED(red=16,green=18,blue=20)
dtpin = Pin(14,Pin.IN,Pin.PULL_UP)
clpin = Pin(15,Pin.IN,Pin.PULL_UP)
rbtn = Pin(13,Pin.IN,Pin.PULL_UP)

value = True
pvalue = False
rvalue = 0
gvalue = 0
bvalue = 0
cycle = "r"
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
writeuwu = Write(oled, ubuntu_mono_20)
def rotary_changed():
    oled.fill(0)
    global pvalue
    global value
    global rvalue,gvalue,bvalue
    global cycle
    if rvalue < 0:
        rvalue = 0
    elif rvalue > 255:
        rvalue == 255
    if gvalue < 0:
        gvalue = 0
    elif gvalue > 255:
        gvalue == 255
    if bvalue < 0:
        bvalue = 0
    elif bvalue > 255:
        bvalue == 255
    if pvalue != clpin.value():
        if clpin.value() == False:
            if dtpin.value() == False:
                if cycle == "r":
                    if rvalue < 255:
                       rvalue = rvalue + 5
                    else:
                        print("already 255!")
                        
                elif cycle == "g":
                    if gvalue < 255:
                       gvalue = gvalue + 5
                    else:
                        print("already 255!")
                        
                elif cycle == "b":
                    if bvalue < 255:
                       bvalue = bvalue + 5
                    else:
                        print("already 255!")
                        
                rgb.color = (rvalue,gvalue,bvalue)
            else:
                if cycle == "r":
                    if rvalue > 0:
                       rvalue = rvalue - 5
                    else:
                        print("already 0!")
                        
                elif cycle == "g":
                    if gvalue > 0:
                       gvalue = gvalue - 5
                    else:
                        print("already 0!")
                elif cycle == "b":
                    if bvalue > 0:
                       bvalue = bvalue - 5
                    else:
                        print("already 0!")
                rgb.color = (rvalue,gvalue,bvalue)
        pvalue = clpin.value()
        writeuwu.text("Red: ", 20, 0)
        writeuwu.text("Green: ", 0, 20)
        writeuwu.text("Blue: ", 10, 40)
        
        writeuwu.text(str(rvalue),60,0)
        writeuwu.text(str(gvalue),60,20)
        writeuwu.text(str(bvalue),60,40)
        oled.show()
    if rbtn.value() == 0:       
        if cycle == "r":
            cycle = "g"
        elif cycle == "g":
            cycle = "b"
        elif cycle == "b":
            cycle = "r"
        utime.sleep(1)
        

while True:
   rotary_changed()
