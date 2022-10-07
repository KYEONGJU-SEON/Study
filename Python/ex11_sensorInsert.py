import time
import spidevRead as sr
import DBConn as dc

while True :
    sensorValue = sr.analog_read(0)#채널번호 0
    print(sensorValue)
    time.sleep(5)
    
    dc.sensorDataInsert(sensorValue)