f = open('srinath.txt')
print(f.tell()) # will say the position of the file pointer.
print(f.readline())
print(f.tell())
print(f.readline())
f.seek(20) # f.seek(the positon where we want to reset out file pointer) willl start the again from that point .
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
f.close()
