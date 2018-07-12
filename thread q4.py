from threading import *
def factorial(num):
    '''Recursive Function to find Factorial'''
    if num == 1:
         return 1
    else:
         return (num * factorial(num-1))
    return 1 if num == 1 else (num * factorial(num-1))


num = int(input("Enter Number to be factorial:"))
print('Factorial of {} is {}'.format(num, factorial(num)))

t=Thread(target=factorial,args=(num,))
t.start()
