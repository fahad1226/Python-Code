

a,b = list(map(int, input ().split ()))

#a,b = list(map(float,input('enter two values ').split()))


try:

    print('school open')
    print(a/b)
    x = int(input('enter an integer '))
    print(x)

except ZeroDivisionError as e:

    print('sorry ,u cant divide something by zero,the problem is ',e)

except ValueError as e:

    print('Invalid input')

except Exception as e:
    print('spmething went wrong')

finally:    #it will execute whatever the exception is
        print('School closed')
