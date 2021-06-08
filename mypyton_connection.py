import os
import pymysql


username=os.getenv('USER')

connection=pymysql.connect(host='localhost',user=username,
                            password='',db='Chinook')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql="select * from Artist" 
        cursor.execute(sql)
        for row in cursor:
            print(row)

finally:connection.close()                                   