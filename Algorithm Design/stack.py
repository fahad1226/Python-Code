
s = [1,2,3,4,5,6,7,8,9]

def push(x):
    k = len(s)
    s[k-1] = x
    k+=1
    print(s)
def pop():
    
    s.pop()
    print(s)

x = int(input())
push(x)
pop()

