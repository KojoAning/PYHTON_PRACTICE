a = [ 1,5,7,8,11,13,16,20,25,47,56,71,8,91,123,144,196,225]

def binerysearch(a,key,start,end):
    if start<= end:
        mid = int(start+end/2)
        if a[mid]>=key:
            return binerysearch(a,key,start,mid -1 )
        elif a[mid]<key:
            return binerysearch(a,key,mid +1 ,end)
    else:
        return a[mid]
    print(key, "could not found ")