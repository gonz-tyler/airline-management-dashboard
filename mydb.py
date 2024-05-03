import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'SoftwareEngineering123!'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE airline_database")
print('all done')