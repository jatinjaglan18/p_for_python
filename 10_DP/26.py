#Buy & sell stocks two transactions allowed

n = int(input('No. of days: '))
arr = [int(input()) for i in range(n)]
k = int(input('No. of transactions: '))

def stock(arr,k):
    dp = [[0 for j in range(len(arr))] for i in range(k+1)]

    for t in range(1,len(dp)):
        ans_max = float('-inf')
        for d in range(1,len(dp[0])):
            if dp[t-1][d-1] - arr[d-1] + arr[d] > ans_max:
                ans_max = dp[t-1][d-1] - arr[d-1] + arr[d]
            '''lmax = float('-inf')
            for i in range(d):
                pot = arr[d] - arr[i] + dp[t-1][i]
                if pot > lmax:
                    lmax = pot'''
            dp[t][d] = max(ans_max, dp[t][d-1])
    
    return dp[k][len(arr)-1]

print(stock(arr,k))