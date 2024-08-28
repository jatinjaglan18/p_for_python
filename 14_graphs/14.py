#dijkstra algo

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

src = int(input('Source: '))
from queue import PriorityQueue
def dijkstra(graph,src):
    visited = [False for i in range(len(graph))]
    pq = PriorityQueue()
    pq.put((0,src,str(src)))        #weight, source, path

    while pq.qsize() > 0:
        val = pq.get()
        if visited[val[1]] == False:
            print(val[1],'vai',val[2],'@',val[0])
        visited[val[1]] = True

        for i in range(len(graph[val[1]])):
            nbr = graph[val[1]][i][1]
            nbr_wt = graph[val[1]][i][2]
            if visited[nbr] == False:
                pq.put((val[0] + nbr_wt, nbr, val[2] + str(nbr)))

dijkstra(graph,src)