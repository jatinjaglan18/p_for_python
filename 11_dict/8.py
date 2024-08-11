#sort nearly sorted array
size = int(input('Size: '))
arr = [int(input()) for i in range(size)]

from queue import PriorityQueue

pq = PriorityQueue()
k = int(input('k: '))
sort_arr = []
for i in range(len(arr)):
    if pq.qsize() < k + 1:
        pq.put(arr[i])
    else:
        sort_arr.append(pq.get())
        pq.put(arr[i])

while pq.qsize() > 0:
    sort_arr.append(pq.get())
print(sort_arr)