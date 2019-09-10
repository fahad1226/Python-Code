
import mysql.connector

con = mysql.connector.connect(host='localhost',user='root',passwd='',database='python')

mycursor = con.cursor()

#mycursor.execute("select * from university_information")

sql = "INSERT INTO university_information(Name,Id,Email,Address,CGPA) VALUES(%s,%s,%s,%s,%s)"
name = input('Enter Name ')
Id = input('Enter Id ')
email = input('Enter Email ')
Address = input('Enter Address ')
cg = float(input('Enter CGPA '))

values = (name,Id,email,Address,cg)

result = mycursor.execute(sql , values)
con.commit()
print(mycursor.rowcount,"record inserted")

#res = mycursor.execute("SELECT * FROM university_information")
#res = mycursor.fetchall()
#for each_element in res:
#    print(each_element)
