#Maximum sum Non adjacent elements

s = int(input())
arr = [int(input()) for i in range(s)]

def m_sum_non_adjacent(arr):
    inc = arr[0]
    exc = 0
    
    for i in range(1,len(arr)):
        ninc = exc + arr[i]
        nexc = max(exc,inc)

        inc = ninc
        exc = nexc
    
    return max(inc,exc)

print(m_sum_non_adjacent(arr))