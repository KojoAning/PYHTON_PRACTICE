import pickle
#pikling a python object
# cars = ['BMW','AUDI','Range Rover','Merceedes'] # THIS COULD HAVE ANY PYTHON OBJECT
# file = 'mycar.pkl'
# fileonject=open(file,'wb')
# pickle.dump(cars,fileonject)
# fileonject.close()

# depickling
file = 'mycar.pkl'
fileobj = open(file,'rb') # rb - read binary
mycar = pickle.load(fileobj)
print(mycar)
