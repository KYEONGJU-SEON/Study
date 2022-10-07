import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
gpio.setup(19, gpio.OUT)
gpio.setup(20, gpio.OUT)

while True:
        # 저항을 마이너스에 연결해둠
    for i in range(18,21,1):
        gpio.output(i, gpio.HIGH) #5볼트(플러스)를 연결한것과 똑같은 효과 
        time.sleep(0.5)
        gpio.output(i, gpio.LOW) # GROUND(마이너스)를 연결한것과 똑같은 효과 
        time.sleep(0.5)
        # 저항을 플러스에 연결할 경우 , LOW 신호에 불이 켜지게 된다.
