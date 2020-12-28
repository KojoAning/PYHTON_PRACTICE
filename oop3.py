class Employee():
    no_of_leave= 8

    def __init__(self,aname , asaalary, arole): # init func. don't requires no calling
        self.name = aname
        self.salary  = asaalary
        self.role = arole


    def printditails(self):
        return f"name is {self.rohan} and salary is {self.salary} and role is {self.role}"

    pass




harry = Employee('harry', 40384 ,'instructur')
rohan = Employee('rohan',10338,'student')# construtor
# rohan = Employee()
#
# harry.name = 'harry'
# harry.salary = 40384
# harry.role='instrucure'
#
# rohan.name ="Rohan"
# rohan.salary = 45555
# rohan.role = "Student"
print ( harry.salary)
print(rohan.role)