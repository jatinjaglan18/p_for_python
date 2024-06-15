#Duplicate Brackets
n = input()

stack = []
for i in range(len(n)):
    if n[i] == ')':
        if stack[len(stack)-1] == '(':
            print(True)
            break
        else:
            while stack[len(stack)-1] != '(':
                stack.pop()
            stack.pop()
    else:
        stack.append(n[i])

else:
    print(False)