#Targeted Sum

n = int(input('Size of Array: '))
s = int(input('Targeted Sum: '))
l = []
for i in range(n):
    val = int(input())
    l.append(val)

def targeted_Sum(arr,idx,set,sum,tar):
    if idx == len(arr):
        if sum == tar:
            print(set)
        return
    
    targeted_Sum(arr,idx+1,set + str(arr[idx]) + ' ', sum + arr[idx], tar)
    targeted_Sum(arr,idx+1,set, sum , tar)
    
targeted_Sum(l,0,'',0,s)