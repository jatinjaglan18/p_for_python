#Coin change combination
s = int(input('size: '))
arr = [int(input()) for i in range(s)]
tar = int(input('Target: '))

def coin_change_combinations(arr,tar):
    dp = [0 for i in range(tar+1)]
    dp[0] = 1
    for j in range(len(arr)):
        val = arr[j]
        for i in range(val,tar+1): 
            dp[i] = dp[i] + dp[i-val]   
    
    return dp[tar]
                    
print(coin_change_combinations(arr,tar))