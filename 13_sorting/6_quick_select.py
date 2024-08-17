#Quick select
s = int(input())
arr = [int(input()) for i in range(s)]
k = int(input())
def partioning(arr,l,r,k):          
    i = l
    j = l
    while i <= r:
        if arr[i] > k:
            i += 1
        else:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j += 1

    return j-1

def quick_select(arr,l,r,k):
    
    pivot = arr[r]
    pi = partioning(arr,l,r,pivot)
    if k-1 == pi:                           #k-1 is for index
        return arr[pi]
    elif k-1 < pi:
        return quick_select(arr,l,pi-1,k)
    else:
        return quick_select(arr,pi+1,r,k)


print(quick_select(arr,0,len(arr)-1,k))