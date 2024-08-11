#Merge k Sorted lsits

n = int(input('No. of lists: '))
arr = []
for i in range(n):
    n_r = input().split(',')
    r = []
    for j in n_r:
        r.append(int(j))
    arr.append(r)

from queue import PriorityQueue
pq = PriorityQueue()
for i in range(n):
    pq.put((arr[i][0],i,0))     #value, row, col

while pq.qsize() > 0:
    v = pq.get()
    print(v[0])
    
    row = v[1]
    col = v[2]
    
    if col < len(arr[row])-1:
        col = v[2] + 1
        pq.put((arr[row][col],row,col))



    