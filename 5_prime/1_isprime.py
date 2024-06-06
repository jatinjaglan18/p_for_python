t = int(input("How many numbers to check: "))

for i in range(t):
    j = int(input("Enter the number to check: "))

    for a in range(2,int(j**0.5)):       # ** repersent as exponential ; it is used find out Square root
        if j % a == 0:
            print(j,'is not a prime number')
            break
    else: 
        print(j, "is a prime number")