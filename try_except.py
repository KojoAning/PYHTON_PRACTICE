#try and except is generally used in working with internet connectivity.

num1 = input("Enter 1st number:")
num2 = input("Enter 2nd number:")
try:
    print( int(num1) + int(num2),'is the result.')
except Exception as e:    #the error is catched as e nd printed
    print(e)
"""The try block lets you test a block of code for errors. The except block lets you handle the error. 
The finally block lets you execute code, regardless of the result of the try- and except blocks. """
print('compiler has reached the end.')