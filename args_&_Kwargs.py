# def function_name_print(a,b,c,d):
#     print(a,b,c,d)
# def fun(*args):
#     print(args[0])
# function_name_print("harry","Rohan","hammad","shivam")

def func(n,*args,**kwargs): # order matters, like normal , *args , **kwargs
    print(d)
    for items in args :
        print(items)
    print("\nand people with their profession:")
    for key,value in kwargs.items():
         print(f"\n{key} is a {value}.")


sri = ["ram","shayam","ramlal","pyarelal","totelal","raju","baburow",
       "nell","nitin","mukesh"]
d="The name of candidates are :"
kw=  {"harry":"coder", "muskesh":"businnessman" , "nill":"crimal" , "rohan":"comedian" ,"rampyari":"artist"}

func(d,*sri,**kw)