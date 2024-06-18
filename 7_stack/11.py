#Prefix Evaluation and Conversion
n = input()

def operations(a1, a2, opr):
    if opr == '+':
        return a1 + a2
    elif opr == '-':
        return a1 - a2
    elif opr == '*':
        return a1 * a2
    elif opr == '/':
        return a1 / a2
    
def post_opreations(a1, a2, opr):
    return a1 + a2 + opr

def in_operations(a1,a2,opr):
    return '('+ a1 + opr + a2 +')'


val = []
infix = []
post = []
for i in n[::-1]:
    if i.isdigit():
        val.append(int(i))
        infix.append(i)
        post.append(i)

    else:
        a1 = val.pop()
        a2 = val.pop()
        val.append(operations(a1,a2,i))

        a1 = infix.pop()
        a2 = infix.pop()
        infix.append(in_operations(a1,a2,i))

        a1 = post.pop()
        a2 = post.pop()
        post.append(post_opreations(a1,a2,i))

print(val[-1])
print(infix[-1])
print(post[-1])