for i in range (99):
    print(i**2)



a = [ ['harry',2],['srinath',8],['jogi',5],['bhubuni',9]]
dict1= dict(a)
print(a)

for i,z in dict1.items() :
     print(i,z)

for i in dict1:  #this will get us only the keys of the dict.
    print(i)

for i,z in (a):
    if z>5 :
        print(i,z)