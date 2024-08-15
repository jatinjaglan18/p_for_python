#Buy & sell stocks infinite no. of transactions with cool down

n = int(input())
arr = [int(input()) for i in range(n)]

def stock(arr):
    obsp = -arr[0]
    ossp = 0
    ocsp = 0

    for i in range(1,len(arr)):
        nbsp = 0
        nssp = 0
        ncsp = 0

        #Buying state
        if ocsp - arr[i] > obsp:
            nbsp = ocsp - arr[i]
        else:
            nbsp = obsp
        
        #selling state
        if arr[i] + obsp > ossp:
            nssp = arr[i] + obsp
        else:
            nssp = obsp 
        
        #cool down
        if ossp > ocsp:
            ncsp = ossp
        else:
            ncsp = ocsp

        obsp = nbsp
        ossp = nssp
        ocsp = ncsp

    return ossp 

print(stock(arr))
        

