def finder(): # when our function is taking much time for initializing we use corouties.
    import time
    book = ['srinath','vikrama', 'rohan', 'ayush', 'abinash']
    time.sleep(3) #this time is being taken for running som heavy task

    while True:
        name  = (yield)
        if name in book :
            print(f'{name} is in the book')

        else:
            print(f'{name} is not in the book ')


# accessing the coroutines
l = finder()
print('searching....')
next(l) # this will take the initial time

l.send('srinath') # using corouties we do not have to go through the inital processing of thr function

l.send('vikrama') # using corouties we do not have to go through the inital processing of thr function

l.close()
