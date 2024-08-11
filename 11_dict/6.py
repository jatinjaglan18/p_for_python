#Priority Queue
from queue import PriorityQueue

pq = PriorityQueue()
arr = [2,10,5,17,7,18,6,4]
for i in arr:
    pq.put(i)       #add in queue acc. to priority

while pq.qsize() > 0:   
    print(pq.get()) #give & pop the highest priority element
