
class Stack:

    def __init__(self):

        self.stack = []

    def push(self,datavalue):

        if datavalue not in self.stack:
            self.stack.append(datavalue)
            return True
        else:
            return False

    def peek(self):

        return self.stack[len(self.stack)-1]


    def pop(self):

        if len(self.stack)<=0:
            
            print('No Elements in stack')

        return self.stack.pop()

FirstStack = Stack()
FirstStack.push(1)
FirstStack.push(29)
FirstStack.push(10)
one = FirstStack.peek()
print(one)
FirstStack.push(23)
two = FirstStack.peek()
print(two)
FirstStack.push('Fahad')
FirstStack.push('CSE')
print(FirstStack.peek())

FirstStack.pop()
print(FirstStack.peek())
