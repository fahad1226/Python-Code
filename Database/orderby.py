
import mysql.connector

con = mysql.connector.connect(host='localhost',user='root',passwd='',database='python')

mycursor = con.cursor()


#sql = "select * from university_information order by id"

sql = "DELETE FROM university_information WHERE Name = %s ";
nm = "name"               #sql injection for safety
mycursor.execute(sql,nm)

con.commit()
result = mycursor.fetchone()

print(mycursor.rowcount, "record(s) deleted")
