
class Queue:

    def __init__(self):

        self.queu = list()

    def push(self,data):

        if data not in self.queu:

            self.queu.insert(0,data)

            return True
        else:
            return False

    def size(self):

        return len(self.queu)


    def showqueue(self):

        for each_element in self.queu:

            print(each_element)


    def remove(self):

        if len(self.queu)>0:
            return self.queu.pop()

        else:
            return "no elements in Queue"


ob = Queue()

ob.push("fahad")
ob.push(1226)
ob.push('fahadbinmnr@gmail.com')
ob.push('Game of thrones')
print(ob.size())
print(ob.showqueue())
ob.remove()
print(ob.showqueue())
