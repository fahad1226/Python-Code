

def fibo(num):

    if num <= 1:
        return num
    else:
        return fibo(num-2)+fibo(num-1)

res = fibo(200) #for this input it takes so much time,recursion always does this.shitty ass
print(res)
