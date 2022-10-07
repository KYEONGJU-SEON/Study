import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

def ledOn():
    gpio.output(18,gpio.HIGH)
    
def ledOff():
    gpio.output(18,gpio.LOW)