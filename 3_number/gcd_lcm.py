'''
1. You are required to print the Greatest Common Divisor (GCD) of two numbers. 
2. You are also required to print the Lowest Common Multiple (LCM) of the same numbers. 
3. Take input "num1" and "num2" as the two numbers. 
4. Print their GCD and LCM.
'''
i = int(input())
j = int(input())

k = min(i,j)
l = max(i,j)

while l % k != 0:
    rem = l % k
    k = rem 
    l = k
    
print('GCD is:', k)
z = (i*j) // k 
print('LCM is:', z)

