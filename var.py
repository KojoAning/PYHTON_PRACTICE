var1 = 'srinath is  '
var2 = 'coder.'# <class 'str'>
var3 = 98 # <class 'int'>
var4= 19.# <class 'float'>
var5='12'
var6='3'
print(100*"i'm srinath \n") # we can print any str as many times we want by n* before the str.
print(10*str((var5+var6))) # adding two 'str' will give us a string that contains them both.
print(float(var5)+float(var6)) #  we can "type cast" any class of data to any other calss of data.
print(var1 + var2)
print(type(var3)) # code type() says the class of the content.
'''
typecasts =
float() 
str()
int()
funfact: there are only three type of data in python.

'''

# quize 1 - my first calculator
# method 1
n1= int(input("Enter your 1st num:"))
n2 = int(input("Enter your 2nd num:"))
sum = n1 + n2
print('SUM =',sum)
# method 2
print('Enter 1st num:')
n1 = input()
print('Enter 2nd num:')
n2 = input()
print("sum =", int(n1)+int(n2))
