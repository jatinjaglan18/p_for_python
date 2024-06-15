#Balanced Brackets
n = input()

stack = []
def balancing(stack, c_b):
    if len(stack) == 0:
        return False

    elif stack[len(stack)-1] == c_b:
        stack.pop()
        return

    else:
        return False
        
for i in n:
    if i == '(' or i == '{' or i == '[':
        stack.append(i)
    
    elif i == ')':
        val = balancing(stack,'(')
        if val == False:
            print(val)
            break

    elif i == '}':
        val = balancing(stack,'{')
        if val == False:
            print(val)
            break
    elif i == ']':
        val = balancing(stack,'[')
        if val == False:
            print(val)
            break
else:
    if len(stack) > 0:
        print(False)
    else:
        print(True)