
days = {'saturday','sunday,monday,tuesday,wednesday','thursday','friday'}
months = set(['January','february','march','april','may','june','july','august','september','october','november','december'])
dates = {21,1,2017}
print(dates)
print(months)
print()
print()

#print(months[2]) we cant do this,set doesent support indexing

days.add('fuckingday')
print(days)
days.discard('fuckingday')
print(days)



a = {1,2,3,4}
b = {4,5,6,2}

uni = a | b #union of two set

print(uni)

inter = a & b #intersection
print(inter)

diff = a - b
print(diff)
