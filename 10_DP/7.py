#Target Sum subsets
s = int(input('size: '))
arr = [int(input()) for i in range(s)]
tar = int(input('Target: '))
def target_sum(arr,tar):
    dp = [[False for j in range(tar+1)] for i in range(len(arr) + 1)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0 :
                dp[i][j] = False
            elif j == 0 :
                dp[i][j] = True

            else:
                
                if dp[i-1][j]:
                    dp[i][j] = True
                else:
                    val = arr[i-1]
                    if j >= val:
                        if dp[i-1][j-val]:
                            dp[i][j] = True
    
    return dp[len(arr)][tar]

print(target_sum(arr,tar))