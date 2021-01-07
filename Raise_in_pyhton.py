# a = input("enter your name : ")
# b= int(input("enter your salary : "))
# if a.isnumeric():
#     raise Exception("numbers are not defined.")
# if b == 0 :
#     raise Exception("zero is not defined as salary:")
#
# print(f"{a} earns {b} rupees.")


c = input("enter your name : ")
try:
    print(a)
except Exception as e :
    if c =='harry':
        raise ValueError("harry is blocked to use it . ")