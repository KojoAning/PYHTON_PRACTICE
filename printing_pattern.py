a =  int(input('How many row to you want : '))
b = int(input('Type 1 for ascending and 0 for descending prints : '))
c = bool(b)
if c == True:
    for i in range(1,a+1):
        for j in range(1,i+1):
            print('*',end=" ")
        print()
elif c == False:
    for i in range(a,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()


