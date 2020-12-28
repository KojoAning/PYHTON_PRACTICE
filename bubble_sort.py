
a=[88,81,44,22,42,51,21,42,11,21,93]

def bubblesort():
    for j in range (0,len(a)-1):
        for i in range(j):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]



bubblesort()
print(a)