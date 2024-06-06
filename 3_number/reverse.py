i = int(input())

def revers(i):

    rev_num=0
    while i>0:
        num = i % 10

        rev_num = (rev_num * 10) + num

        i = i // 10

    return rev_num

rev_num = revers(i)

print(rev_num)

#check palindrome
print(int(rev_num)==i)