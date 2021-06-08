import os
import pymysql
import datetime

username=os.getenv('USER')

connection=pymysql.connect(host='localhost',user=username,
                            password='',db='Chinook')

try:
    with connection.cursor() as cursor:
        row=('vikas',42,'1978/11/28')
        cursor.execute("insert into SCHOOL values(%s, %s, %s);",row)
        connection.commit()

finally:connection.close()                                   