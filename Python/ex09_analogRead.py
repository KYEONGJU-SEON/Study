import spidevRead as sr
import time

while True :
    sensorValue = sr.analog_read(0)#채널번호 0
    print(sensorValue)
    time.sleep(0.5)
    
