#Coin Change Permutations
s = int(input('size: '))
arr = [int(input()) for i in range(s)]
tar = int(input('Target: '))

def coin_change_permutations(coins,tar):
    dp = [0 for i in range(tar+1)]
    dp[0] = 1
    for i in range(1,len(dp),1):
        for coin in coins:
            if coin <= i:
                dp[i] = dp[i] + dp[i-coin]
    return dp[tar]

print(coin_change_permutations(arr,tar))