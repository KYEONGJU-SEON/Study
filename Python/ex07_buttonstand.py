import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
gpio.setup(21,gpio.IN)
cnt = 0
check = True
    
p = gpio.PWM(18,500)
p.start(0)

while True :
    buttonState=gpio.input(21)
    print(buttonState)

    if buttonState == 1:
        if check == True :
            cnt+=1
            check = False
            if cnt==1:
                p.ChangeDutyCycle(100)
            elif cnt == 2 :
                p.ChangeDutyCycle(50)
            elif cnt == 3:
                p.ChangeDutyCycle(0)
                cnt = 0                
    else :
        check = True 