class PriorityQueue:
    def __init__(self):
        self.arr = []           #heap -> Complete Binary Tree
        pass                    #heap -> Heap order property

    def add(self,val):
        self.arr.append(val)
        self.upheapify(len(self.arr) - 1)

    def upheapify(self,idx):
        if idx == 0:
            return 
        
        parent = (idx-1)//2
        if self.arr[idx] < self.arr[parent]:
            self.swap(idx,parent)
            self.upheapify(parent)

    def swap(self,idx,parent):
        #self.arr[idx],self.arr[parent] = self.arr[parent],self.arr[idx]
        temp = self.arr[idx]
        self.arr[idx] = self.arr[parent]
        self.arr[parent] = temp

    def remove(self):
        if len(self.arr) == 0:
            print('Priority queue is empty')
            return -1
        else:
            self.swap(0,-1)
            val = self.arr.pop()
            self.downheapify(0)
            return val

    def downheapify(self,idx):
        sci = idx
        
        lci = (2*idx) + 1
        rci = (2*idx) + 2
        
        if lci < len(self.arr) and self.arr[lci] < self.arr[sci]:
            sci = lci
        
        elif rci < len(self.arr) and self.arr[rci] < self.arr[sci]:
            sci = rci
        
        if sci != idx :
            self.swap(idx,sci)
            self.downheapify(sci)

    def peek(self):
        if self.size == 0:
            print('Priorit queue is empty')
            return -1
        else:
            return self.arr[0]

    def size(self):
        return len(self.arr)
    

class PriorityQueueReversed():
    def __init__(self):
        self.arr = []

    def add(self,val):
        self.arr.append(val)
        self.upheapify(len(self.arr) - 1)

    def upheapify(self,idx):
        if idx == 0:
            return 
        
        parent = (idx-1)//2
        if self.arr[idx] > self.arr[parent]:
            self.swap(idx,parent)
            self.upheapify(parent)

    def swap(self,idx,parent):
        self.arr[idx],self.arr[parent] = self.arr[parent],self.arr[idx]   

    def remove(self):
        if self.size() == 0:
            print('Empty')
        else:
            self.swap(0,-1)
            val = self.arr.pop()
            self.downheapify(0)
            return val

    def downheapify(self,idx):
        sci = idx
        lci = (2*idx) + 1
        rci = (2*idx) + 2

        if lci < self.size() and self.arr[lci] > self.arr[sci]:
            sci = lci
        if rci < self.size() and self.arr[rci] > self.arr[sci]:
            sci = rci

        if sci != idx:
            self.swap(idx,sci)
            self.downheapify(sci)

    def peek(self):
        if self.size() == 0:
            print('Empty')
        else:
            return self.arr[0]

    def size(self):
        return len(self.arr)
