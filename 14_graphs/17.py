#iterative DFS

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
def iterative_dfs(graph,s):
    visited = {}
    stack = [[s,str(s)]]

    while stack:
        val = stack.pop()
        if val[0] not in visited:
            print(val[0], '@', val[1])
        visited[val[0]] = True
        for i in range(len(graph[val[0]])):
            nbr = graph[val[0]][i][1]
            if nbr not in visited:
                stack.append([nbr,val[1] + str(nbr)])
iterative_dfs(graph,src)