#Infix Evaluation

def perecedence(opr):
    if opr == '+':
        return 1
    elif opr == '-':
        return 1
    elif opr == '*':
        return 2
    elif opr == '/':
        return 2
    else:
        return 0
    
def operations(a1, a2, opr):
    if opr == '+':
        return a1 + a2
    elif opr == '-':
        return a1 - a2
    elif opr == '*':
        return a1 * a2
    elif opr == '/':
        return a1 / a2


n = input()

stack_opr = []
stack_oprnd = []

for i in n:
    if i.isdigit():
        stack_oprnd.append(int(i))

    elif i == '(':
        stack_opr.append(i)

    elif i == ')':
        while stack_opr[-1] != '(':
            a2 = stack_oprnd.pop()
            a1 = stack_oprnd.pop()
            opr = stack_opr.pop()

            val = operations(a1,a2,opr)

            stack_oprnd.append(val)

        #it pop '('
        stack_opr.pop()
    
    elif i == '+' or i == '-' or i == '*' or i == '/':

        #opr wants to solve high or equal precendence 
        while len(stack_opr) != 0 and i != '(' and perecedence(i) <= perecedence(stack_opr[-1]):
            a2 = stack_oprnd.pop()
            a1 = stack_oprnd.pop() 
            opr = stack_opr.pop()
            val = operations(a1,a2,opr)
            stack_oprnd.append(val)


        #opr push
        stack_opr.append(i)

while len(stack_opr) != 0:
    a2 = stack_oprnd.pop()
    a1 = stack_oprnd.pop()
    opr = stack_opr.pop()
    val = operations(a1,a2,opr)

    stack_oprnd.append(val)

print(stack_oprnd[-1])
        