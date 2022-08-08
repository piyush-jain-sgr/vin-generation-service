import re
import mysql.connector as mysql
myconnection = mysql.connect(
    user='root',
    port='3306',
    password='Tel@12345',
    host='127.0.0.1', database='vinnumbers', auth_plugin='mysql_native_password'
)
mycursor = myconnection.cursor()
vinnumber="vinnumber";
SQl_query = "INSERT INTO allvinnumbers (VIN) VALUES ('"+vinnumber+"')"
mycursor.execute(SQl_query)
myconnection.commit()