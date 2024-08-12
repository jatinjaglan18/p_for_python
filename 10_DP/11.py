#0-1 knapsack

n = int(input('No. of items: '))
weight = [int(input()) for i in range(n)]
value = [int(input()) for i in range(n)]
capacity = int(input('Capacity: '))
def knapsack(w,v,cap):
    dp = [[0 for i in range(cap+1)] for j in range(len(w)+1)]
    
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i > 0 and j > 0:
                v1 = dp[i-1][j]
                if j - w[i-1] <= i :
                    v2 = v[i-1] + dp[i-1][j - w[i-1]]
                    val = max(v1,v2)
                else:
                    val = v1
                
                dp[i][j] = val

    return dp[len(w)][cap]

print(knapsack(weight,value,capacity))