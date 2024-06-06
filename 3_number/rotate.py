'''
Question Statement: 
1. You are given two numbers n and k. You are required to rotate n, k times to the right. If k is positive, rotate to the right i.e. remove rightmost digit and make it leftmost. Do the reverse for negative value of k. Also k can have an absolute value larger than number of digits in n.
2. Take as input n and k.
3. Print the rotated number.
4. Note - Assume that the number of rotations will not cause leading 0's in the result. e.g. such an input will not be given
   n = 12340056
   k = 3
   r = 05612340
'''

i = int(input())
k = int(input())

n = 0 
temp = i
while temp > 0:
    n += 1
    temp = temp // 10

if k < 0:
    k = n + k

k = k % n
while k > 0:

    rem = i % 10
    r = rem * (10**(n-1))
    i = i // 10
    i = i+r
    k -= 1

print(i)
