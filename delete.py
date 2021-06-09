import os
import pymysql
import datetime

username=os.getenv('USER')

connection=pymysql.connect(host='localhost',user=username,
                            password='',db='Chinook')

try:
    with connection.cursor() as cursor:
        cursor.execute("delete from SCHOOL where name='smith';")
        connection.commit()

finally:connection.close()                                   