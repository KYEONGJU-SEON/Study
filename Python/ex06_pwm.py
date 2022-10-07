import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)

p = gpio.PWM(18,500)
p.start(0)

while True:
    p.ChangeDutyCycle(0)
    time.sleep(0.5)
    p.ChangeDutyCycle(50)
    time.sleep(0.5)
    p.ChangeDutyCycle(100)
    time.sleep(0.5)
    