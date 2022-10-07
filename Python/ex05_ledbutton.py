import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
gpio.setup(21,gpio.IN)
cnt = 0
check = True
    
while True :
    buttonState=gpio.input(21)
    print(buttonState)

    if buttonState == 1:
        if check == True :
            cnt+=1
            check = False
            if cnt % 2==1:
                gpio.output(18, gpio.HIGH)
            else :
                gpio.output(18, gpio.LOW)    
    else :
        check = True
        

    