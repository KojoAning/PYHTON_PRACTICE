# built in function
a = 8
b = 2
c =  sum((a,b))
print (c)

#user difened fuction
def ave(a,b):
    """docstrings: this functions calculates average """
    average = ( a +b)/2 # the "average" will give the average
    return average # return average = ave(a,b)= "average"

v = ave(100,10) # ave will call the fuction and the value will be asigned to the a & b .
print (v)
print (ave.__doc__) # (function.__doc__) will print the 1st statement in the fuction .