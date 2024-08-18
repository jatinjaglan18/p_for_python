vertex = int(input('Vertex: '))
edges = int(input('Edges: '))
def graph(vertex,edges):
    graph = {}
    print('Vertex')
    for i in range(vertex):
        #v = input()
        graph[i] = []

    print('Edges')
    for i in range(edges):
        ipt = input().split(' ')
        v1 = int(ipt[0])
        v2 = int(ipt[1])
        wt = int(ipt[2])

        graph[v1].append((v1,v2,wt))
        graph[v2].append((v2,v1,wt))

    return graph
        
graph = graph(vertex,edges)

src = int(input('Source: '))
des = int(input('Destination: '))
visted = {}
for i in graph.keys():
    visted[i] = False

#ceil and floor & small and large & kth largest path
wt = int(input('Weight: '))
k = int(input('kth largest: '))
sp = ''
lp = ''
sw = float('inf')
lw = float('-inf')
wtc = float('inf')
wtf = float('-inf')
gcpath = '' 
gfpath = ''

from queue import PriorityQueue
pq = PriorityQueue()

def small_large_ceil_floor(graph,s,d,path,w,v):
    global wtc
    global wtf
    global gcpath
    global gfpath
    global sw
    global lw
    global sp
    global lp
    global pq
    global k 

    if s == d:
        pa = path + str(d)
        if pq.qsize() == k:
            pq.get()
        pq.put((w,pa))
        #small path
        if w < sw:
            sw = w
            sp = pa
        
        #large path
        if w > lw:
            lw = w
            lp = pa

        #ceil
        if w > wt and w < wtc:
            wtc = w
            gcpath = pa

        #floor
        if w < wt and w > wtf:
            wtf = w
            gfpath = pa


    v[s] = True
    for i in range(len(graph[s])):
        nbr = graph[s][i][1]
        wsn = graph[s][i][2]
        if v[nbr] == False:
            small_large_ceil_floor(graph,nbr,d,path+str(s),w + wsn,v)       
    v[s] = False

small_large_ceil_floor(graph,src,des,'',0,visted)
print(sp,'@',sw)
print(lp,'@',lw)
print(gcpath,'@',wtc)
print(gfpath,'@',wtf)
val = pq.get()
print(val[1], '@', val[0])
