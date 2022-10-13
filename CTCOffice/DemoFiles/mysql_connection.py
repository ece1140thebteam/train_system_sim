import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P1ttsburgh"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE ctcoffice")

print(mydb)