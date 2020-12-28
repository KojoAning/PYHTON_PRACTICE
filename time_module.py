import time

initial = time.time()


l=0
while ( l< 10):
    print("aham bramhasmi")
    time.sleep(2)
    l+=1
print("while loop took",time.time()-initial,"secs")
initial2 = time.time()
for i in range (11):
    print('\naham bramhasmi')
print("for loop took",time.time()-initial,"secs")


locacltime = time.asctime(time.localtime(time.time()))
print(locacltime)