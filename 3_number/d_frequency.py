n = int(input())
k = int(input())

def count_fre(n,k):
    count = 0
    while n > 0 :
        digit = n % 10
        if digit == k :
            count += 1
        
        n = n// 10

    return (count)

print(count_fre(n,k))