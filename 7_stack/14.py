#Smallest Number Following Pattern d ->, i -< 

n =input()

stack =[]
a = 1
stack.append(a)
for i in n:
    if i == 'd':
        a += 1
        stack.append(a)
    else:
        while len(stack) != 0:
            print(stack.pop(), end='')
        a += 1
        stack.append(a)


while len(stack) != 0:
    print(stack.pop(), end='')