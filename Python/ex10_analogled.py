import ledCon as lc
import time
import spidevRead as sr


while True :
    sensorValue = sr.analog_read(0)#채널번호 0
    print(sensorValue)
    time.sleep(0.5)
    
    if sensorValue<700:
        lc.ledOn()
    else :
        lc.ledOff()
