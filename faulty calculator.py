#designing a calculator that will perform all the calculation right accept the folowing
# 45*3=555, 56+9=66, 95/2=4
n1 = int(input("Enter your first value:"))
opt = input('Enter your opretion:')
n2 = int(input("Enter your second value:"))

if opt == "+":
     result = n1 + n2
     if n1 == 56 and n2 == 9 :
         result = 77
if opt == "*":
    result = n1 * n2
    if n1 == 45 and n2 == 3 :
        result = 555
if opt == "/":
    result = n1/n2
    if n1 == 56 and n2 == 6 :
        result=4

print("your calculated answer is :",result)