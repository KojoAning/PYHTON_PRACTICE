# dict. is nthing except a key value pair.
d = {"harry":"burger","amit":"fish","srinath":"mutton","subham":{"B":"Maggi","L":"chawal","D":"paneer"}}
d[420]='junk food' # value of key can either be a int. or a string , but the value can be of any dta type :)
print(d)
a = d.copy()     # when we add the code .copy() , then a and d won't be the same. any change in d won't reflect in a .
del d[420]
print(a.get('harry')) # the code - nameofdict.get("name of key whose value we want to access") will give us the respective value of the key
d.update({"leena":"toffee"}) #.update will add the enterd dict item into the list to the end
print(d)
print(a.keys()) # the code '.key' will provide all the keys(only) inside the dict.
print(a.items()) # .items wil provide all the key value pairs in the dict.
