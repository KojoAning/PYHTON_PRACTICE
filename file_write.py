# f = open("srinath2.txt", "w")  # a - append mode = the content we are entring now will add up to the end .
# # w - write mode means only the content we are providing now will stay in the file.
# a=f.write('\nSrinath is comitted to jogi.\n')
# print(a) # this will give the number of charecters printed the file.
#
# f.close()

f = open ('srinath.txt','r+') # r+ is the mode syntex for both read and write the file.
print(f.read())
f.write('thank you')
 