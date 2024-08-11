#k largest element in array
size = int(input('Size: '))
arr = [int(input()) for i in range(size)]

from queue import PriorityQueue

pq = PriorityQueue()
k = int(input('k: '))
for i in range(len(arr)):
    if i < k :
        pq.put(arr[i])
    else:
        peek = pq.get()
        if arr[i] > peek:
            pq.put(arr[i])
        else:
            pq.put(peek)
print(pq.qsize())
while pq.qsize() > 0:
    print(pq.get())
