class Youtuer:
    def __init__(self,name,catagory):
        self.Name = name
        self.Catagory = catagory
        # self.email = f'{name}.{catagory}@gmail.com'

    def string(self):
        return f"Name of the Youtuber is {self.Name} and there content catagory is {self.Catagory}."
    @property # function can be used as an atribute
    def email(self):
        if self.Name==None:
            return 'email is not set'
        else:
            return self.Name+self.Catagory+'@email.com'


    @email.setter
    def email(self,given_email):
        a = given_email.split("@")[0]
        self.Name = a.split('.')[0]
        self.Catagory= a.split('.')[1]

    @email.deleter
    def email(self):
        self.Name =None
        self.Catagory = None

if __name__ == '__main__':


    code_with_harry = Youtuer('Harry','programming')
    tanmay_bhat=Youtuer("tanmmy",'Comady')


    # print(tanmay_bhat.email)
    # code_with_harry.Catagory = "coding"
    # print(code_with_harry.email)
    code_with_harry.email= 'programer.harry@emil.com'
    # print(code_with_harry.email)
    # del code_with_harry.email
    # print(code_with_harry.email)
    print(code_with_harry.Catagory)