# ---------------it better to avoid mulit level inheritance------------------
# because --------->>>>>>>>>>


class A :
    def mot(self):
        print('from class A')
class B(A):
    def mot(self):
        print('from class B')
    pass
class C(A):
    def mot(self):
        print('from class C')
    pass
class D(B,C):
    def mot(self):
        print('from class D')
    pass


a = A()
b=B()
c =C()
d =D()

d.mot()