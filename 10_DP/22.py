#buy & sell stock

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