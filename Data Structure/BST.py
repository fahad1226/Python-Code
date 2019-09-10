
class Node:

    def __init__(self,data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):

        if self.left:
            self.left.printTree()
        print(self.data,end=' ')
        if self.right:
            self.right.printTree()


    def Search_Tree(self,value):

        if value < self.data:
            if self.left is None:
                return print(str(value)+" value is not found")
            return self.left.Search_Tree(value)
        elif value > self.data:
            if self.right is None:
                return print(str(value)+" value is not found")
            return self.right.Search_Tree(value)

        else:
            print(str(self.data)+' is found')


root = Node(10)
root.insert(23)
root.insert(32)
root.insert(23)
root.printTree()
print()
root.Search_Tree(243)
