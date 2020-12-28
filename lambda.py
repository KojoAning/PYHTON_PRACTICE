#lambda function is also known as anonymous function
# def add (a,b):
#     return a+b
# n = add(4,5)
n = lambda a , b : a+b
print(n(5,4))

# def first(k):
#     return k[0]
k = [ [5,9],[2,1],[9,1]]
k.sort(key=lambda k:k[1]) #this key will only take a name of function
print(k)