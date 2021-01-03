class Employee:




    def __init__(self,skill,experiance,salary):

        self.skil=skill
        self.experiance = experiance
        self.salary=salary
    def isopen(self,day):
        if day == 'sunday' or 'saturday':
            return "chuti hai ajj !!"
        else:
            return "no chuti."

    def incremanet(self,by_percent):
        self.salary = int(self.salary*by_percent)
        return f'Salary is incresed by {by_percent}%. just print self.salary to get you incremented salary'

    @ property
    def email(self):
        if self.first_name == None:
            return 'Email is deleted'

        else:
            mail = self.first_name+'.'+self.last_name+'@gamil.com'
            return mail


    @email.setter
    def email(self,given_email):
        mail = given_email.split('@')[0].split('.')
        self.first_name = mail[0]
        self.last_name = mail[1]

    @email.deleter
    def email(self):
        self.first_name =None
        self.last_name =None

    def __add__(self , other):
        return self.salary+other.salary
    def __repr__(self):
        return f"Employee('{self.skil}', '{self.experiance}', {self.salary})" # this is how a __repr__ should be used
    def __str__(self):
        return 'this is a string'
if __name__ == '__main__':
    harry = Employee('software Engineer','6 yeras', 90000)
    srinath = Employee('ML Engineer','1 year',70000)

#________________________________________________command area _________________________________________
a=srinath+harry
print(a)
print(srinath) # __str__>__repr__
print(repr(srinath)) # thus we have to specify it . 