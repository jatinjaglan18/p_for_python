#Perfect friends

n = int(input('No. of friends: '))
k = int(input())


def graph(v,e):
    graph = {}
    for i in range(n):
        graph[i] = []

    for i in range(e):
        ipt = input().split()
        v1 = int(ipt[0])
        v2 = int(ipt[1])

        graph[v1].append((v1,v2))
        graph[v2].append((v2,v1))

    return graph

graph = graph(n,k)

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
    for i in range(len(g.keys())):
        if v[i] == False:
            comp = []
            tree(g,i,comp,v)
            res.append(comp)

    return res

comp = get_components(graph,visited)
print(comp)

pairs = 0

for i in range(len(comp)):
    for j in range(i+1,len(comp),1):
        pairs += len(comp[i]) * len(comp[j])
print(pairs)