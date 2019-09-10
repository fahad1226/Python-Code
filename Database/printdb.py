
import mysql.connector

con = mysql.connector.connect(host='localhost',user='root',passwd='',database='python')

mycursor = con.cursor()

#mycursor.execute('SELECT * FROM university_information')
mycursor.execute('SELECT Name,Address from university_information')
result = mycursor.fetchall()

for each_element in result:

    print(each_element)

print()
print()

mycursor.execute('select name,CGPA from university_information')

result = mycursor.fetchone()
for each_element in result:

    print(each_element)
