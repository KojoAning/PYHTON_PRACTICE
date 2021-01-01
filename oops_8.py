class Employee():


    def __init__(self,first_name,last_name,skill,experiance,salary):
        self.first_name = first_name
        self.last_name=last_name
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

class player():
    a=1

    def __init__(self,name,game):
        self.name= name
        self.game =game

class cool_prog(Employee,player): # mulltiple inheritance

# sequence matters
# interpreter will look for Employee and then in player for a variable
    def printlang(self):
        print('c++')

if __name__ == '__main__':
    harry = Employee('Harrish','aggarwal','software Engineer','6 yeras',90000)
    srinath = Employee('Srinath','Shrestha','ML Engineer','1 year',70000)
    karan = player('karan',['cricket','footbal','table tannis'])
    nill = cool_prog('Nill','kamal','MEMER','6 months',10000,) # this can inharit single class. which is 1st entered.
    # despit the construter we can acces all the atributs and methods of these two class




#________________________________________________command area _________________________________________
