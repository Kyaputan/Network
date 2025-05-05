import mysql.connector
import os

DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD="310146"
DB_NAME="My_SQL"

try:
    mydb = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    port=3306
    )  
except mysql.connector.Error as err:
    print(f"Error: {err}")
    
    
mycursor = mydb.cursor(dictionary=True)
sql = "SELECT * FROM User;"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)