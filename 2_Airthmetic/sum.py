i = int(input())

def sum_even_odd(i):
    even = 0
    odd = 0 
    while i > 0:
        num = i % 10
        if num % 2 == 0:
            even += num
        elif num % 2 != 0 :
            odd += num
        
        i = i // 10
    
    print(even, odd)

sum_even_odd(i)

