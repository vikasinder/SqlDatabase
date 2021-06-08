import os
import pymysql
import datetime

username=os.getenv('USER')

connection=pymysql.connect(host='localhost',user=username,
                            password='',db='Chinook')

try:
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS SCHOOL(NAME CHAR(20), AGE INT,DOB datetime);""") 
        
     

finally:connection.close()                                   