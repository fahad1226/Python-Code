
#show the graph vertices

class Graph:

    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}  #create a dictionary
        self.gdict = gdict

    def getvertices(self):

        return list(self.gdict.keys())

    def addvertex(self,vertex):

        if vertex not in self.gdict:
            self.gdict[vertex] = []

graph_elements = {'a':['b','c'],
                 'b':['a','d'],
                 'c':['a','d'],
                 'd':['c','b','e'],
                 'e':['d']
                 }

vertices = Graph(graph_elements)
vertices.addvertex('r')
vertices.addvertex('f')
vertices.addvertex('a') #eta nibena karon eta ekbar ache
show = vertices.getvertices()
print(show)
