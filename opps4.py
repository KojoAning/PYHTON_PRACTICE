class Employee():
    no_of_leave= 8
    def __init__(self,aname , asaalary, arole): # init func. don't requires no calling
        self.name = aname
        self.salary  = asaalary
        self.role = arole
    def printditails(self):
        return f"name is {self.rohan} and salary is {self.salary} and role is {self.role}"
    @classmethod
    def chnge_leaves(cls , newleaves):
        cls.no_of_leave = newleaves


harry = Employee('harry', 40384 ,'instructur')
rohan = Employee('rohan',10338,'student')# construtor

harry.chnge_leaves(33)

print (harry.no_of_leave)
