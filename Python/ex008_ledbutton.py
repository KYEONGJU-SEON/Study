import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
gpio.setup(21,gpio.IN)

p = gpio.PWM(18,500)
p.start(0)

buttonState=gpio.input(21)
print(buttonState)

while True:
    #100까지 가야하니까 range(101)해줘도됨. 
    for i in range(0,100,1):
         p.ChangeDutyCycle(i)
         time.sleep(0.01)
         
    for i in range(100,0, -1):
        p.ChangeDutyCycle(i)
        time.sleep(0.01)
