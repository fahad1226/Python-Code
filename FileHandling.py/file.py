

f = open("mydata","r")

print(f.read())


#f = open('notepad','w')
#x = input('enter text')
#f.write(x)

f1 = open('fahad1226.jpg','rb')
f2 = open('fahad.jpg','wb')

for i in f1:

    f2.write(i)
