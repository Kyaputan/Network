import mysql.connector
from loadex05 import load_env_ex05


db_host ,db_user ,db_password = load_env_ex05()

try:
    mydb = mysql.connector.connect(
        host=db_host, user=db_user, password=db_password, database="MySQL"
    )
except mysql.connector.Error as err:
    print(f"Error: {err}")

mycursor = mydb.cursor()
sql = "select * FROM world.countrylanguage;"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    
