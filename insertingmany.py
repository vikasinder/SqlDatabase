import os
import pymysql
import datetime

username=os.getenv('USER')

connection=pymysql.connect(host='localhost',user=username,
                            password='',db='Chinook')

try:
    with connection.cursor() as cursor:
        rows=[('john',41,'1982/1/18'),('kali',23,'1938/1/28'),('smith',42,'1985/11/8'),('karry',47,'1973/11/28')]
        cursor.executemany("insert into SCHOOL values(%s, %s, %s);",rows)
        connection.commit()

finally:connection.close()                                   