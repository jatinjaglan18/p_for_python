#Decode strings

string = input()

def decode(s):
    dp = [0 for i in range(len(s))]
    dp[0] = 1

    for i in range(1,len(s)):
        if s[i-1] == '0' and s[i] == '0':
            dp[i] = 0
        elif s[i-1] == '0' and s[i] != '0':
            dp[i] = dp[i-1]
        elif s[i-1] != '0' and s[i] == '0':
            if int(s[i-1]) == 1 or int(s[i-1]) == 2:
                if i >= 2 :
                    dp[i] = dp[i-2] 
                else:
                    dp[i] = 1
        else:
            dp[i] = dp[i-1]
            if int(s[i-1:i+1]) <= 26:
                if i >= 2:
                    dp[i] += dp[i-2]
                else:
                    dp[i] += 1
    return dp[-1]
print(decode(string))
            


        