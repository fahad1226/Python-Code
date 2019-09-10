
import time

def is_prime(n):

    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


#for num in range(1,21):

#    print(num,is_prime(num))  #yes,its correctly identifies the prime numbers....but how  fast is this function??????


t0 = time.time()

for n in range(1,10000):

    is_prime(n)

t1 = time.time()

print('time required for this functions is ',t1 - t0)
