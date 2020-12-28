


def greet(count):
    if count == 0:
        return
    else:
        print ("hii")
        count = count - 1
    greet()



greet(10) # need to stop the recursion