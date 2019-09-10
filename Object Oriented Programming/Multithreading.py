
#  amra kono code likhle okhane ekta thread must thake,which is main Thread


from time import sleep
from threading import *

class Hello(Thread):

    def run(self):

        for i in range(5):
            print('Hello')
            sleep(1)


class Hi(Thread):

    def run(self):

        for i in range(5):
            print('Hi')
            sleep(1)

o1 = Hello()
o2 = Hi()
o1.start()
sleep(0.1)
o2.start()
o1.join()
o2.join() # join() method main thread ke opekkha korte boltese tar execution shesh hobar jonno

print('Good Bye') #main thread শেষে এটাকে কল করবে এন্ড এক্সিকিউট করবে
