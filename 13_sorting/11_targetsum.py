#target sum pair

s = int(input())
arr = [int(input()) for i in range(s)]
tar = int(input())
def target_sum_pair(arr,tar):
    arr.sort()
    i = 0 
    j = len(arr) - 1

    while i < j:
        pot = arr[i] + arr[j]
        if pot > tar:
            j -= 1
        elif pot < tar:
            i += 1
        else:
            print(arr[i],arr[j])
            i += 1
            j -= 1

target_sum_pair(arr,tar)
        

