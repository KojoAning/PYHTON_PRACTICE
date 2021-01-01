class Var:
    public = 31
    _protected=232
    __privet= 34

    pass

harry = Var()
print(harry._protected)

try:
    print(harry.__privet) # this will give error because the variable is privet
except:
    print(harry._Var__privet,'- ECEPTION')