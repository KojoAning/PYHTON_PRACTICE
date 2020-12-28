
l = 10 # global var
def funtion1(n):
    # l = 5 # local var
    m = 8
    global l # we need this syntex for changing the global var
    l = l+45  # we can't change the value of the global var. unless " global var"
    print(l,',',m)
    print(n, '\nprinted')


funtion1('this is me . ')

"""print(m) # we can't print local var out side a fun."""


def srinath():
    x = 20
    def sri () : # this fuct. created a global var 88
        global x
        x = 88
    print( 'before calling srinath()',x)
    sri()
    print("after calling srinath()",x)


srinath()
print(x)