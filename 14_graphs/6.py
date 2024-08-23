#is connected 

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


def tree(g,s,c,v):
    v[s] = True
    c.append(s)

    for i in range(len(g[s])):
        nbr = g[s][i][1]
        if v[nbr] == False:
            tree(g,nbr,c,v)

def get_components(g,v):
    res = []
    for i in range(vertex):
        if v[i] == False:
            comp = []
            tree(g,i,comp,v)
            res.append(comp)

    return res

comp = get_components(graph,visited)
if len(comp) == 1:
    print(True)
else:
    print(False)