#Unbounded Knapsack

n = int(input('No. of items: '))
weight = [int(input()) for i in range(n)]
value = [int(input()) for i in range(n)]
capacity = int(input('Capacity: '))

#permutation
def knapsack(w,v,cap):
    dp = [0 for i in range(cap+1)]

    for i in range(1,len(dp)):
        for j in range(len(w)):

            if w[j] <= i:
                val = v[j] + dp[i-w[j]]
                if dp[i] < val:
                    dp[i] = val
    return dp[cap]

print(knapsack(weight,value,capacity))
