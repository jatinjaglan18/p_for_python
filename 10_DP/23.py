#Buy & sell stocks infinite no. of transactions with selling fee

n = int(input())
arr = [int(input()) for i in range(n)]

fee = int(input('Selling Fee: '))

def stock(arr,fee):
    obsp = -arr[0]
    ossp = 0
    
    for i in range(1,len(arr)):
        nbsp = 0
        nssp = 0

        #new buying state profit
        if ossp - arr[i] > obsp:
            nbsp = ossp - arr[i]
        else:
            nbsp = obsp
        
        #new selling state profit
        if arr[i] + obsp - fee > ossp:
            nssp = arr[i] + obsp - fee 
        else:
            nssp = ossp

        obsp = nbsp
        ossp = nssp

    return ossp


print(stock(arr,fee))


