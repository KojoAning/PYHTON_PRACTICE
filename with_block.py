# def gettime():
#     import datetime
#     return datetime.datetime.now()
# value=input("type here\n")
# with open('srinath.txt') as op : # this includes opening and closing a file .
#     op.write(str([str(gettime())]) + ": " + value + "\n")           # here we can give our commands to the interpreter.
#     print ('DONE')




with open('srinath.txt') as a :
    m = a.read()
    print(m)

f =  open('srinath.txt')
 # print(f.readlines())
print (f.readline())
f.close()