import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(21,gpio.IN) # 신호를 읽어오니까 IN
gpio.setup(20,gpio.OUT)

while True :
    buttonState =gpio.input(21)
    print(buttonState)
    time.sleep(0.01)
    
    if buttonState==1:
        gpio.output(20, gpio.HIGH)
    else :
        gpio.output(20, gpio.LOW)
        