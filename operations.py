"""Ø Arithmetic operators ---> + , -, /, *, %  (modulus),   //,  **
Ø Assignment operators ----> += (if a= 5, b = 3 , a += b {AKA a = a +  b }then a will be 8) , -=  , *=   ,  / =  ,  %= ,  //=  , **=   (used to assign something  )
Ø Relation/ Comparison Operators ----> ==,  != (not equal to ) , < , > , <= , >= (greater than equal)"""
# operateros in python :-

#Arithmetic Operators
#Assignment Operators
#comperision operators
#logicl operators
#idenity operators
#membership operators
#Bitwise Operator

#Arithmetic Operators
print("5+6 is",5+6)
print("5-6 is",5-6)
print("5*6 is",5*6)
print("5/6 is",5/6)
print("5//6 is",5//6)
print("5**6 is",5**6) # expontial operstord
print("5%6 is",5%6) # reminder

#Assignment Operators
x = 5
x+=7  # similarly we have -= , /= , %= ,
print(x)# it will give 12 because x = x+7 where x is the new variable and x is 5

#comperision operators
i=5
print (i == 5 , i >5, i<5,i != 5 ,i <= 5)

#Logical operators (and),(or),(not)
a = True
b= False
print(a and b)
"""True n false = false
True n True = false
True or false = true
true ir true = true 
"""
# Identity Operators
print ( 5 is not 5)
print ( 5 is 5 )

# Membership operators
list = [ 3,2,1,5,6,8,9,0]
print ( 32 in list)
print ( 3 not in list)
print ( 3 in list)

# Bitiwise operation
# o - 00
"""1 n 0 = 0
1 n 1 = 1
 1 or 0 = 1
 1 or 1 = 1"""
# 1 - 01
# 2 - 10
# 3 - 11
print(0|3)
print(0&3)
print(0&1)
print(0|1)

