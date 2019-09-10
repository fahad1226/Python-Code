
import collections

dic1 = {'day1':'monday','day2':'friday','day3':'wednesday'}
dic2 = {'day3':'thursday','day2':'sunday','day5':'satday'}

res = collections.ChainMap(dic1,dic2)

print(res.maps,'\n')

print('keys = {} '.format(list(res.keys())))
print('values = {}'.format(list(res.values())))

print('Elements in map')

for key,value in res.items():

    print('{} = {}'.format(key,value))



print()
print()

print('day 1 in res {}'.format('day 1' in res))
