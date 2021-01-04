'''
itrable - __getitem / __iter__ is defined in this object. ( this can give itrator)
itrator -  a object in which next method is defined ( we can get into the next element of a itrator )
itration -  to itrate a element and fetch it's next element is called itration
generators -  a itrator which can be used only one
'''
def gen(n):
    for i in range (n):
        yield i # this will produce the number on the fly which saves our ram from being filled with number

a = gen(10000) # now a is a obj which have the generator to gen 10000th number
# when we have less RAM and bigger numbers we can use gen to generate, by this the no.s wouldn't get strored in our ram
print(a)


# for i in gen(10000):
#     print(i)


b = gen(4)
print(next(b)) # this no. is not saved
print(next(b)) # this no. is not saved
print(next(b)) # this no. is not saved
print(next(b)) # this no. is not saved
print(next(b)) # this no. is not saved
print(next(b))

# Lists, tuples, str,  dictionaries, and sets are all iterable objects


