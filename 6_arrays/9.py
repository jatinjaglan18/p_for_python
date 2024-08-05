#subsets
s = int(input())
arr = [int(input()) for i in range(s)]

limit = 2 ** len(arr) #No. of subsets

for i in range(limit):
    print(i)
    string = ''
    for j in range(len(arr) - 1, -1 , -1):   #reverse loop because at 1st we get last value of pur bit

        #binary
        r = i % 2
        i = i // 2

        if r == 0 :
            string = '_ ' + string 
        else:
            string = str(arr[j])+ ' ' + string

    print(string)