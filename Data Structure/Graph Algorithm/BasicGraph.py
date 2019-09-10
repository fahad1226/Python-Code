
import collections

graph = {'a':['b','c'],
        'b':['a','d'],
        'c':['a','d'],
        'd':['c','d','e'],
        'e':['e']
}

for each_element in graph:
    print(each_element)

res = collections.ChainMap(graph)

for key,value in res.items():

    print('Nodes {} = Edges {} '.format(key,value))
