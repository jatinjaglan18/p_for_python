#count binary string with no consecutive 0's
n = int(input())
def count_binary(n):
    b0 = 1      #count of strings ends with 0
    b1 = 1      #count of strings ends with 1

    for i in range(2,n+1):
        b_1 = b0 + b1
        b_0 = b1

        b0 = b_0
        b1 = b_1

    return b0+b1

print(count_binary(n))