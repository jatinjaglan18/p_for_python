#Buy & sell stocks two transactions allowed

n = int(input())
arr = [int(input()) for i in range(n)]

def stock(arr):
    dps = [0 for i in range(len(arr))]
    dps[0] = 0
    buy = arr[0]

    for i in range(1,len(arr)):
        profit = arr[i] - buy
        if profit < 0:
            buy = arr[i]
            dps[i] = dps[i-1]
        
        elif profit > dps[i-1]:
            dps[i] = profit

        else:
            dps[i] = dps[i-1]

    dpb = [0 for i in range(len(arr))]
    dpb[-1] = 0
    sell = arr[-1]
    for i in range(len(arr) - 2, -1 , -1):
        profit = sell - arr[i]
        if profit < 0:
            sell = arr[i]
            dpb[i] = dpb[i+1]
        elif profit > dpb[i+1]:
            dpb[i] = profit
        else:
            dpb[i] = dpb[i+1]

    profit = 0 
    for i in range(len(arr)):
        if dps[i] + dpb[i] > profit:
            profit = dps[i] + dpb[i]
    
    return profit

print(stock(arr))
