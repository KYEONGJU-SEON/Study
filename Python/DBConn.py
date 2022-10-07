import pymysql as ps

#msql db 연결
db = ps.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    db = "test",
    charset = "utf8"
    )
# Cursor Object 가져오기 
# SQL 실행하기
# 실행 mysql 서버에 확정 반영하기
# DB연결 닫기

curs = db.cursor()

def sensorDataInsert(s):
    sql = f'insert into sensordb(sensing) values({s})'
    curs.execute(sql)
    db.commit()
    
#Cursor Object 가져오기
#SQL 실행하기
#mysql서버로부터 데이터 가져오기 : fetch 메서드 사용(fechall/fetchmany/fetchone)
    
def sensorDataSelect():
    sql = 'select * from sensordb'
    curs.execute(sql)
    result = curs.fetchall()
    return result

"""
r = sensorDataSelect()
print(r)
print(len(r))
print(r[0])
print(r[0][1])
print(type(r[0][1]))

"""
    