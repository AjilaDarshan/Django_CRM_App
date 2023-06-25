import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root2luffy//-'
)

#prepare a cursor

cursorObject = dataBase.cursor()

#create a database

cursorObject.execute("CREATE DATABASE babygroot")

print("ALL DONE!")