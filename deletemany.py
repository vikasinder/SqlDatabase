import os
import pymysql
import datetime

username=os.getenv('USER')

connection=pymysql.connect(host='localhost',user=username,
                            password='',db='Chinook')

try:
    with connection.cursor() as cursor:
       rows= cursor.executemany("delete from SCHOOL where name= %s;",['john','vikas'])
       connection.commit()

finally:connection.close()                                   