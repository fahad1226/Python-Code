
import heapq

heap = [21,23,11,45,32,78,99]
heapq.heapify(heap)   # smallest value ta sobar age ashbe,bakigula sorted hobena

print(heap)

heapq.heappush(heap,6) #inserting value into heap
print(heap)

heapq.heappop(heap) # first index delete hoye jabe

print(heap)

heapq.heapreplace(heap,6) #always replace the smallest element
print(heap)
