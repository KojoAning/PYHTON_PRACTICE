class Employee:#class won't be empty always
    no_of_leaves= 8 # this is a object of class

    pass

harry = Employee()
rohan = Employee()

harry.name = 'harry'
harry.salary = 40384
harry.role='instrucure'

rohan.name ="Rohan"
rohan.salary = 45555
rohan.role = "Student"

print (harry.salary)
print(rohan.role)
print(harry.role)
# we can acces the object of the class through the elements of class or variables
print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)

# changing the objects
print (Employee.__dict__) # this will  returns a dict. which have all the class objects on the class 
Employee.no_of_leaves= 9
# rohan.no_of_leaves = 9 # tying to chnge the object by the variables (this wil not work )
print('the new one is',Employee.no_of_leaves)





