#spread infection

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

src = int(input('Has Infection: '))
time = int(input('How much time: '))
visited = [0 for i in range(vertex)]

def spread_infection(graph,src,time,v):
    count = 0
    q = [[src,1]]

    while q:
        val = q.pop(0)

        if val[1] > time:
            break
        
        if v[val[0]] == 0:
            v[val[0]] = val[1]
            count += 1

        for i in range(len(graph[val[0]])):
            nbr = graph[val[0]][i][1]
            if v[nbr] == 0:
                q.append([nbr,val[1] + 1])
    return count

print(spread_infection(graph,src,time,visited))