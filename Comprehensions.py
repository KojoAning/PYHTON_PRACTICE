#==================(in typical method)======================
# lis =[]
# for i in range(100):
#     if i%7==0:
#         lis.append(i)
# print(lis)

#--------------------------in list comprehansion-----------------------------
lis=[i for i in range(100) if i%7==0]
# print(lis)

#============================================================================
dict_1 = {0:'item 0',1:"item 1"} # and so on
# print(dict_1)
# ------------------------------------------------------------------------
dict_smarter = {i:f'item {i}' for i in range(1,10)} # we can even apply a condition
# print(dict_smarter)
dict_smarter = {value:key for key,value in dict_smarter.items()} # revers the key value pair
# print(dict_smarter)
# -----------------------------------------------------------------------------------------------------------
set = {i for i in ['dress 1','dress 2','dress 1','dress 2','dress 1','dress 2']} # items don't repeat in sets
# print(set)
# ------------------------------------------(generator comprehensions)-------------------------------------------------------------------
evens = (i for i in range(1,101) if i%2==0)# parenthesis is the differece b/w generators and lis ( this is way to creat a generate in one line)
# print(evens)
# to itrate the values
# for item in evens: print(item)

# _______________________________________________________________Exersice_____________________________________________________
n = input("Enter one of the following \n (list / dict / set ) : ")

if n =="list":
    k = int(input("enter the no. till you want to expand your list "))
    list = [i for i in range(k+1)]
    print(list)
elif n =='dict':
    m = int(input("enter the last limit of the dict element "))
    dictnary = {i:f'item {i}' for i in range(m+1)}
    print(dictnary)

else:
    l = input("enter element to your set by space : ")
    list_set = (l.split( ))
    s = {i for i in list_set}
    print(s)
