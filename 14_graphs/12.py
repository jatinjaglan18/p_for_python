#Bipartite graph


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

def isbipartite(g,s,v):
    q = [[s,0]]      #source , level
    while q:
        val = q.pop(0)

        if v[val[0]] != -1:
            if val[1] != v[val[0]]:
                return False
        
        else:
            v[val[0]] = val[1]

        for i in range(len(g[val[0]])):
            nbr = g[val[0]][i][1]
            if v[nbr] == -1:
                q.append([nbr,val[1] + 1])

    return True

visited = [-1 for i in range(vertex)]

for i in range(vertex):
    if visited[i] == -1:
        res = isbipartite(graph,i,visited)

        if res == False:
            print(False)
            break

else:
    print(True)

