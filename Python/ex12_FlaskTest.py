from flask import Flask , render_template
import ledCon as lc
import DBConn as dc


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('main.html') #웹 데이터에 띄워줄 응답 메세지

@app.route("/led/on")
def led_on():
    lc.ledOn()
    return "ON!"

@app.route("/led/off")
def led_off():
    lc.ledOff()
    return "OFF!"

@app.route("/sensor")
def getSensor():
    result = dc.sensorDataSelect()
    r = '<br>'.join(map(str, result))
    return r 

if __name__ == '__main__' :
    app.run(host = '172.30.1.15')
 
 
"""
__name__
직접실행됏을때 - main
import해서 실행됐을때 모듈이름
"""