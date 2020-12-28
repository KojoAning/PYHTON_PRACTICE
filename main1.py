def sum(a,b) :
    return a+b

def my_str(string):
    return f"my name is {string}"

print(f"this is {__name__}")
if __name__ == '__main__': #while importing this file the following function will not get imported due to this code
    print(my_str("srinath"))
    c = sum(5,2)
    print(c)