#Merge sort
s1 = int(input())
arr1 = [int(input()) for i in range(s1)]

s2 = int(input())
arr2 = [int(input()) for i in range(s2)]

#sorted array
def merge(arr1,arr2):
    arr = []

    s1 = len(arr1)
    s2 = len(arr2)

    i = 0
    j = 0 

    while i < s1 and j < s2:
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1

        
    while i < s1:
        arr.append(arr1[i])
        i += 1
    
    while j < s2:
        arr.append(arr2[j])
        j += 1
    
    return arr

#print(merge(arr1,arr2))

def merge_sort(arr,l,r):
    if l == r:
        return [arr[l]]
    
    mid = (l+r)//2
    left = merge_sort(arr,l,mid)
    right = merge_sort(arr,mid+1,r)
    return merge(left,right)

print(merge_sort(arr1,0,len(arr1)-1))