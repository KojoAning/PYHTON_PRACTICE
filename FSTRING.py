# f string is = fast string


a= 'and i\'m '
b='stylish'
# c= 'i am srinath %s %s '%(a,b)
# c= 'i\'m srinath {0} {1}'
# n=c.format(a,b)
n = f'i\'m srinath {a} {b} {math.tan(45)}'
print(n)