n1 = int(input("Enter your Age:"))
if n1>18 and n1 <100 :
    print("You can drive.")
elif n1 == 18:
    print("You can apply for DL.")
elif n1<18:
    print ("You are under aged for driving.")
else :
    print("illogical Age")