
class Graph:

    def __init__(self,gdict=None):

        if gdict is None:
            gdict = {}
        self.gdict = gdict



    def findedges(self):

        edge = []   # create an empty list of Edges
        for vertex in self.gdict:
            for nextvertex in self.gdict[vertex]:
                if {nextvertex,vertex} not in edge:
                    edge.append({vertex,nextvertex})

        return edge

    def get_edges(self):

        return self.findedges()



graph_elements = {'a':['b','c'],
                 'b':['a','d'],
                 'c':['a','d'],
                 'd':['c','b','e'],
                 'e':['d']
                 }


Edges = Graph(graph_elements)
show = Edges.get_edges()
print(show)
