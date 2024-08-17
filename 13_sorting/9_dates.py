#sort dates

s = int(input())
arr = [input() for i in range(s)]
def count_sort(arr,div,mod,ra):
    
    freq = [0 for i in range(ra)]
    for i in arr:
        d = int(i) // div % mod
        freq[d] += 1
    
    for i in range(1,len(freq)):
        freq[i] = freq[i-1] + freq[i]

    ans = [0 for i in range(len(arr))]
    for i in range(len(arr)-1,-1,-1):
        d = int(arr[i]) // div % mod
        ans[freq[d] - 1] = arr[i]
        freq[d] -= 1
    
    for i in range(len(arr)):
        arr[i] = ans[i]

def dates_sort(arr):
    count_sort(arr,1000000,100,32)          #days

    count_sort(arr,10000,100,13)            #months
    
    count_sort(arr,1,10000,2501)             #year
    

dates_sort(arr)
print(arr)