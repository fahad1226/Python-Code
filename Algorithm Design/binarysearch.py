
def binary_search(list,key):

    low = 0
    high = len(list) - 1
    while low < high:
        mid = (low+high)//2

        if key == list[mid]:
            return mid
        if key > list[mid]:
            low = mid + 1
        else:
            high = mid - 1

        if low > high:
            return None

list = [2,3,2,23,4,4,3,4,35,56,4,34,3]
list.sort()
print('sorted list is ',list)
input = int(input('enter a value to search '))
res = binary_search(list,input)
if res == None:
    print('not found')
else:
    print('value found and index of this value is {} '.format(res))
