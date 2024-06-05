i = int(input())

rev_num=0
while i>0:
    num = i % 10

    rev_num = (rev_num * 10) + num

    i = i // 10

print(rev_num)