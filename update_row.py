import os
import pymysql
import datetime

username=os.getenv('USER')

connection=pymysql.connect(host='localhost',user=username,
                            password='',db='Chinook')

try:
    with connection.cursor() as cursor:
        cursor.execute("update SCHOOL set age=99 where name='karry';")
        connection.commit()

finally:connection.close()                                   