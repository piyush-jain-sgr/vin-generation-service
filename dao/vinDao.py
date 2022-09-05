import mysql.connector
import time
from datetime import datetime
class VinDao:
    def connectToDatabase(self):
        myconnection = mysql.connector.connect(host="localhost",
                                               user="root",
                                               password="Tel@12345",
                                               database="vinnumbers",
                                               auth_plugin='mysql_native_password'
                                               )
        return myconnection
    def insertVinIntable(self, vinNumbers):
        myconnection=self.connectToDatabase()
        mycursor=myconnection.cursor()
        #SQl_query = "INSERT INTO allvinnumbers (VIN) VALUES (%s)"
        now = str(datetime.now())
        for vinnumber in vinNumbers:
            SQl_query = "INSERT INTO allvinnumbers (VIN, created_time) VALUES ('" + vinnumber +"','"+now+"')"
            mycursor.execute(SQl_query)
        myconnection.commit()
    def retreiveAllVin(self):
        myconnection=self.connectToDatabase()
        mycursor=myconnection.cursor()
        sql = '''SELECT * from allvinnumbers '''
        mycursor.execute(sql)
        result = mycursor.fetchall();
        myconnection.close()
        return result
    def retreiveSelectedVin(self, fromTime, toTime):
        myconnection=self.connectToDatabase()
        mycursor=myconnection.cursor()
        sql = "SELECT * FROM allvinnumbers WHERE created_time BETWEEN '"+fromTime+"' and '"+toTime+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall();
        myconnection.close()
        return result