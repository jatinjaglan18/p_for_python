#is cyclic

#Hamiltonian path & cycles

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

graph = graph(vertex,edges)

def iscyclic(graph):
    visited = {}
    for i in graph.keys():
        if i not in visited.keys():
            cycle = traverse(graph,i,visited)
            if cycle:
                print(True)
                return
    print(False)
    return

def traverse(graph,src,visited):
    q = [src]

    while q:
        v = q.pop(0)
        if v in visited.keys():
            return True
        visited[v] = True

        for i in range(len(graph[v])):
            nbr = graph[v][i][1]
            if nbr not in visited.keys():
                q.append(nbr)
            
    return False

iscyclic(graph)
