a = [ 1,9,3,7,5,4,8]

def selectionsort():
    for i in range(len(a)-1):
        mim_value = i
        for j in range(i, len(a)):            
                mim_value=j
        temp= a[i]
        a[i]=mim_value
        mim_value=temp


selectionsort()
print(a)