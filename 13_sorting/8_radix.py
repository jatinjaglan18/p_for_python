#Radix sort

s = int(input())
arr = [int(input()) for i in range(s)]

def count_sort(arr,exp):
    ra = 10

    freq = [0 for i in range(ra)]
    for i in arr:
        d = i // exp % 10
        freq[d] += 1

    for i in range(1,len(freq)):
        freq[i] = freq[i] + freq[i-1]
    
    ans = [0 for i in range(len(arr))]
    for i in range(len(arr)-1,-1,-1):
        #digit at n place
        d = arr[i] // exp % 10
        ans[freq[d]-1] = arr[i]
        freq[d] -= 1 
    
    for i in range(len(arr)):
        arr[i] = ans[i]

def radix_sort(arr):
    ma = float('-inf')
    for i in arr:
        if ma < i:
            ma = i
    
    exp = 1
    while exp < ma:
        count_sort(arr,exp)
        exp = exp * 10

radix_sort(arr)
print(arr)