#Inverse of an array
s = int(input())
arr = [int(input()) for i in range(s)]

res = [0 for i in range(s)]

for i in range(s):
    res[arr[i]] = i

print(res)