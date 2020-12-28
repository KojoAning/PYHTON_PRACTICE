# def factoriacl(n):
#     f = 1
#     for i in range(n):
#         f = f * (i+1)
#     return f
#
# number  = int(input('Enter the number: '))
# print(factoriacl(number))
#

'''
def fibonacci(n):
     if n == 1:
         return 0
     elif n==2:
         return 1
     else:
         return fibonacci(n-1)+fibonacci(n-2)
number = int(input('Enter the number : '))
print(fibonacci(number))'''


n = int(input('enter a number : '))
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range (2,n):
        c=a+b
        a=b
        b=c
        print(c)

print(fib(n))