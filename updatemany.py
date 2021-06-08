import os
import pymysql
import datetime

username=os.getenv('USER')

connection=pymysql.connect(host='localhost',user=username,
                            password='',db='Chinook')

try:
    with connection.cursor() as cursor:
        rows=[(45,'smith'),(37,'kali')]
        cursor.executemany("update SCHOOL set age=%s where name=%s;",rows)
        connection.commit()

finally:connection.close()                                   