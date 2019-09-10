print('hello fahad,welcome to python world')

numbers = [2,1,32,4,5,3,4,3,4,5,64]

even = list(filter(lambda n :n%2==0,numbers))

double = list(map(lambda n:n*2,even))

addall = list(map(lambda n:n**2,even))

print(even)
print(double)
print(addall)
cnt = len(even)

print("total even numbers are {} ".format(cnt))

myarray = [2,2,34,23,34,34,2,34,35,2,3,5]

sq = list(map(lambda n:n**2,myarray)) #etar jonno map use korte hobe not filter()
print(sq)
