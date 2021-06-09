import os
import pymysql
import datetime

username=os.getenv('USER')

connection=pymysql.connect(host='localhost',user=username,
                            password='',db='Chinook')

try:
    with connection.cursor() as cursor:
       rows= cursor.execute("delete from SCHOOL where name= %s;",'kali')
       connection.commit()
   # ALTERNATE UPDATE IS WHERE THERE IS A SPECIFIC RECORD // NOT MULTIPLE ROWS TO BE PASSED
        # SO WE PASS PARTICULAR RECORD INSTEAD OF ROWS AS IN UPDATE MANY
    
finally:connection.close()                                   