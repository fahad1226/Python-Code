
import mysql.connector

con = mysql.connector.connect(host='localhost',user='root',passwd='',database='python')

mycursor = con.cursor()


sql = "SELECT Name,id,Address FROM university_information WHERE Address = %s"
adr = ("hathazari", )

mycursor.execute(sql,adr)

res = mycursor.fetchall()

for each_element in res:

    print(each_element)
