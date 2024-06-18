#Postfix Evaluation and conversion
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
    
def operations(a1, a2, opr):
    if opr == '+':
        return a1 + a2
    elif opr == '-':
        return a1 - a2
    elif opr == '*':
        return a1 * a2
    elif opr == '/':
        return a1 / a2

def pre_operations(a1, a2, opr):
    return opr + a1 + a2

def in_operations(a1,a2,opr):
    return '(' + a1 + opr + a2 + ')'

val = []
pre = []
infix = []
for i in n:
    if i.isdigit():
        val.append(int(i))
        pre.append(i)
        infix.append(i)
    
    elif i == '+' or i == '-' or i == '*' or i == '/':
        a2 = val.pop()
        a1 = val.pop()
        val.append(operations(a1,a2,i))

        a2 = infix.pop()
        a1 = infix.pop()
        infix.append(in_operations(a1,a2,i))

        a2 = pre.pop()
        a1 = pre.pop()
        pre.append(pre_operations(a1,a2,i))

print(val[-1])
print(pre[-1])
print(infix[-1])
        