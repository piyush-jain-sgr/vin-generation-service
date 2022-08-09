import mysql.connector
import time
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
        t = time.time()
        t_ms = str(t)
        for vinnumber in vinNumbers:
            SQl_query = "INSERT INTO allvinnumbers (VIN, created_time) VALUES ('" + vinnumber +"','"+t_ms+"')"
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