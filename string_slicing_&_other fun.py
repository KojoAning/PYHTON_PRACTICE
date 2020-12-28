sring  = 'a string is a collection of charecters in single memory unite'

mystr =  "She loves me so much." # this is a string
print(mystr[-1]) # == print (mystr[::-1])
print(mystr[3])# the argument in [n] will select the 4th element in the from the string
print(mystr[0:5]) # in this argument this much string [n:m=(k-1)] will be printed
# . Here,zero is included but 5 is excluded.
print(len(mystr)) # len() will give the length of a string or list or array
# print(mystr[19]) # this wil through error since there is no 19 character
print(mystr[0:19]) # when the argument askes for more character than the actual one then it wil print the maximum no. of char.
# but only in this format
print(mystr[::]) # by defult [::] = 0:len(str):1 .. 1st - staring point,2nd-endpoint ,3rd- n charaters of gape between the str.
print(mystr[0:9:2]) # 3rd-1 don't skips one one charecters, but 2 does.
print(mystr[-4:-2]) # in minus it start from the end of str. and it start counting from -1,-2,-3,-4,-5...
# this will give result from -4 to -2
print(mystr[-1:-4:-2]) # this will revers the string.
# we should not use  no.s less then -1 on 3rd either in str or in list
print(mystr[::-7])

# fuctions in string
print(len(mystr))
print(type(mystr))
print(mystr.lower())
print(mystr.upper())
print(mystr.isalnum())#returns false when there are char aother than numbers and latters.
print(mystr.isalpha())
print(mystr.endswith('mine'))
print(mystr.count('e'))
print(mystr.capitalize())
print(mystr.find('is'))
print(mystr.replace('is','are'))







