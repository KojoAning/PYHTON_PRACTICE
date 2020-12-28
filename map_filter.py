# numbers = ["3",'98','21',]
# # for i in range(len(numbers)):
# #     numbers[i] = int(numbers[i])
# numbers = list(map(int,numbers))
# numbers[2] = numbers[2]+1
# print(numbers[2])

#----------------map-------------
# num = [2,3,4,5,6,7,8,9]
# squre = list(map(lambda a: a*a,num))
# print(squre)



# def square_function(a):
#     return a*a
# def cube_function(b):
#     return b*b*b
# def oct_function(c):
#     return c**c**c**c
# lis = [square_function,cube_function,oct_function]
# for i in range(9):
#     val = list(map(lambda x: x(i),lis))
#     print(val)

#-------------filter-------------


# list1 = [1,2,3,4,5,6,7,8,9]
# def greater_then_5(n):
#     return n > 5
# gr_then_5 = list(filter(greater_then_5,list1))
# print(gr_then_5)

#---------------------reduce-------------------------

from functools import reduce
lis = [1,2,3,4]
n = reduce(lambda x,y:x+y ,lis)

# n = 0
# for i in lis:
#     n = n+i
print(n)








