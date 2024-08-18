#All paths in graph

vertex = int(input('Vertex: '))
edges = int(input('Edges: '))
def graph(vertex,edges):
    graph = {}
    print('Vertex')
    for i in range(vertex):
        v = input()
        graph[v] = []

    print('Edges')
    for i in range(edges):
        ipt = input().split(' ')
        v1 = ipt[0]
        v2 = ipt[1]
        wt = int(ipt[2])

        graph[v1].append((v1,v2,wt))
        graph[v2].append((v2,v1,wt))

    return graph
        
graph = graph(vertex,edges)

src = input('Source: ')
des = input('Destination: ')

visted = {}

for i in graph.keys():
    visted[i] = False

def paths(graph,s,d,v,path):
    if s == d:
        print(path + d)
        return
    
    visted[s] = True

    for i in range(len(graph[s])):
        nbr = graph[s][i][1]
        if visted[nbr] == False:
            paths(graph,nbr,d,v,path+s)
    
    visted[s] = False
paths(graph,src,des,visted,'')