#Prim's Algo

vertex = int(input('Vertex: '))
edges = int(input('Edges: '))

def graph(vertex,edges):
    graph = {}
    for i in range(vertex):
        graph[i] = []

    print('input for edges: ')
    for i in range(edges):
        ipt = input().split(' ')
        v1 = int(ipt[0])
        v2 = int(ipt[1])
        wt = int(ipt[2])

        graph[v1].append((v1,v2,wt))
        graph[v2].append((v2,v1,wt))
    
    return graph

graph = graph(vertex, edges)
print(graph)
src = int(input('Starting Point: '))

from queue import PriorityQueue
#Minimum Spaning tree
def prims(graph,s):
    visited = [False for i in range(len(graph))]

    pq = PriorityQueue()
    pq.put((0,s,-1))  #weight, source, aquire edge

    while pq.qsize() > 0:
        val = pq.get()
    
        if val[2] != -1 and visited[val[1]] == False:
            print(val[1],'-',val[2],'@',val[0])
        visited[val[1]] = True

        for i in range(len(graph[val[1]])):
            nbr = graph[val[1]][i][1]
            wt = graph[val[1]][i][2]
            if visited[nbr] == False:
                pq.put((wt,nbr,val[1]))

prims(graph,src)