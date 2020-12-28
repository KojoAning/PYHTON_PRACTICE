class Employee():
    no_of_leave= 8
    def __init__(self,aname , asalary, arole): # init func. don't requires no calling
        self.name = aname
        self.salary  = asalary
        self.role = arole
    def printditails(self):
        return f"name is {self.rohan} and salary is {self.salary} and role is {self.role}"
    @classmethod
    def chnge_leaves(cls , newleaves):
        cls.no_of_leave = newleaves
    @classmethod
    def f_str(cls , str):
        return cls(*str.split("-"))

    @staticmethod
    def printgood(str):
        print('this is good '+ str)
        return 89

class programer(Employee):
    number_of_holidays = 56
    def __init__(self,aname , asalary, arole,lang):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.lang=lang
    def printprog(self):
        return f"name is {self.name} and salary is {self.salary} and role is {self.role} and he knows {self.lang}"



harry = Employee('harry', 40384 ,'instructur')
rohan = Employee('rohan',10338,'student')# construtor
# karan = Employee.f_str('karan-11000-engineer')
karan = programer('karan',786,'programer','python')
harry.chnge_leaves(3)

# print (harry.no_of_leave)
print(karan.printprog())
print(karan.number_of_holidays)
