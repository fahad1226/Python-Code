
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',passwd='',database='fahads_databse')

mycursor = mydb.cursor()
mycursor.execute("select * from mytable")

result = mycursor.fetchall() #for all data in databse
#result = mycursor.fetchone() #for one row in database
for i in result:

    print(i)
