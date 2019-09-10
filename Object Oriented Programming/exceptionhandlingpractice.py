


a ,b = list(map(int,input().split()))

try:

    res = a/b
    print(res)
    sqres = res**10
    print(sqres)
    x = float(input('enter an float number '))
    print(x**2)


except ZeroDivisionError as e:

    print("Infinite value can't be calculated")

except ValueError as e:

    print('Invalid input,float wanted')

finally:

    print('python is easy to learn and full of fun')
