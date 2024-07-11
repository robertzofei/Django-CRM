
import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd  = 'admin'
	)

# prepare a cursor object

cursorObject = dataBase.cursor()

# create a database

cursorObject.execute("CREATE DATABASE shelbyco")

print("All done!")