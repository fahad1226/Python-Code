
import math
import time

def is_prime_v2(n):

    if n == 1:
        return False
    max_divisior = math.floor(math.sqrt(n))
    for d in range(2,1+max_divisior):
        if n % d == 0:
            return False
    return True


#for n in range(2,34):
#    print(n,is_prime_v2(n))


#lets see how much tijme it takes to calculate these prime numbers

t0 = time.time()

for n in range(2,10000):
    is_prime_v2(n)

t1 = time.time()

print('time required for this algorithm is ',t1 - t0)  # ৯ সেকন্ড টাইম নিচ্ছে এই এল্গো এর জন্য

#আমরা এটাকে আরো ইম্প্রুভ করতে পারবো।
