# Caching : here we can save the last 'n' number of calls and their input and output for minimizind the processing task.

import time
from functools import lru_cache     #this module is a must
@lru_cache(maxsize = 3)  # this is a decorater and we can save last nth call from maxsize
def work(n):
    #some task taking n secs
    time.sleep(n) #function delay
    return n


if __name__ == '__main__':
    print('runnig some work')
    work(3) # this wouldn't get stored
    work(1) # these values will get stored
    work(2) # these values will get stored
    work(4) # these values will get stored

    print('Done...Calling again') # this task will take no time because we are using the same function with same input
    work(3)
    print('Called again')

