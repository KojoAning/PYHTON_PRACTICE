
# f=open('doesnotexist.txt')


# print('import stuff')
#
f1 = open('mylogs.txt')


try:
   f=open('xyz.txt')
except IOError as e : # there can we multiple exceeption
    print('io erroe hai',e)
except EOFError as e :
    print('eo error hai',e)
except OSError as e :
    print('os error hai',e)
except TabError as e :
    print('tab error hai',e)
except KeyError as e :
    print('key error hai',e)

else: # if excep is not running
    print('except is not running ')

finally: # this is gonna run anyway
    print('running anyway...')
    f1.close()


print('imp stuff')

#
#
# f1 = open('mylogs.txt')
#
# try:
#    f=open('srinath.txt')
# except Exception as e :
#     print(e)
# else:
#     print('except is not running ')
#
# finally: # code cleanup , closing all thr opened file
#     print('running anyway...')
#     f1.close()
#
#
# print('imp stuff')
#





























