#buy & sell stock

#one Transaction
n = int(input())

arr = [int(input()) for i in range(n)]

def stock(arr):
    least = arr[0]
    profit = 0
    for i in range(1,len(arr)):
        nprofit = arr[i] - least
        if nprofit < 0:
            least = arr[i]
        else:
            if nprofit > profit:
                profit = nprofit
    return profit

print(stock(arr))

#Many transactions

def stock1(arr):
    buy = arr[0]
    sell = arr[0]

    profit = sell-buy

    for i in range(1,len(arr)):
        
        if arr[i] >= sell:
            sell = arr[i]
        
        else:
            profit += sell - buy
            buy = arr[i]
            sell = arr[i]
       
    profit += sell - buy

    return profit
print(stock1(arr))

        