#Infix -> Postfix
#Infix -> Prefix

n = input()

def perecedence(opr):
    if opr == '+':
        return 1
    elif opr == '-':
        return 1
    elif opr == '*':
        return 2
    elif opr == '/':
        return 2
    
def pre_operations(a1, a2, opr):
    return opr + a1 + a2

def post_operations(a1,a2,opr):
    return a1 + a2 + opr

stack_pre = []
stack_post = []
stack_opr = []

for i in n :
    if i.isdigit():
        stack_pre.append(i)
        stack_post.append(i)

    elif i == '(':
        stack_opr.append(i)

    elif i == ')':
        
        while stack_opr[-1] != '(':
            opr = stack_opr.pop()

            a2 = stack_pre.pop()
            a1 = stack_pre.pop()
            stack_pre.append(pre_operations(a1,a2,opr))

            a2 = stack_post.pop()
            a1 = stack_post.pop()
            stack_post.append(post_operations(a1,a2,opr))

        stack_opr.pop()

    elif i == '+' or i == '-' or i == '*' or i == '/':

        while len(stack_opr) != 0 and stack_opr[-1] != '(' and perecedence(i) <= perecedence(stack_opr[-1]):
            opr = stack_opr.pop()

            a2 = stack_pre.pop()
            a1 = stack_pre.pop()
            stack_pre.append(pre_operations(a1,a2,opr))

            a2 = stack_post.pop()
            a1 = stack_post.pop()
            stack_post.append(post_operations(a1,a2,opr))

        stack_opr.append(i)

while len(stack_opr) != 0:

    opr = stack_opr.pop()

    a2 = stack_pre.pop()
    a1 = stack_pre.pop()
    stack_pre.append(pre_operations(a1,a2,opr))

    a2 = stack_post.pop()
    a1 = stack_post.pop()
    stack_post.append(post_operations(a1,a2,opr))

print('Prefix:', stack_pre[-1])
print('Postfix:', stack_post[-1])
