#Get connected components

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

visited = []
for i in graph.keys():
    visited.append(False)

def tree(graph, vertex,comp,v):
    v[vertex] = True
    comp.append(vertex)
    
    for i in range(len(graph[vertex])):
        nbr = graph[vertex][i][1]
        if v[nbr] == False:
            tree(graph,nbr,comp,v)

res = []
for i in range(vertex):
    
    if visited[i] == False:
        ans = []
        tree(graph,i,ans,visited)
        res.append(ans)

print(res)