i = int(input())

# count digits of an integer
count = 0
z = i
while z > 0:
    count += 1
    z = z // 10

print(count)

# print every digit of an integer
rem = i
y = 10**(count-1)
while y > 0:
    
    print(rem // y)
    rem = rem % y
    y = y // 10
   
