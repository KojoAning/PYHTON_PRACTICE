f=open("srinath.txt","rt")  # f is a file handle
"""print(f.readlines())""" # this provides a list of line in the txt file
print(f.readline()) # this provides the first line in the text file
print(f.readline())# this provides the next concicutive line in the file
print(f.readline())


''' for line in f:
     print(line, end = "") #this will print the text file  line by line '''
'''F is a file pointer
 insides=f.read(10)
print("1",insides)

insides=f.read(44454) # this works ryt after the privious selected latters in the text file .
print('2',insides)'''
# if we enter a unsenible number in the argument of the read() then the compiler will simplu ignor it and take it as blank.

f.close() # this sets resources frees for the below codes







