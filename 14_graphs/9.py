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

visited = {}

src = int(input('Source: '))

def hamiltonian_path_cycles(g,s,v,p,os):
    
    if len(v) == len(g) - 1:
        
        for i in range(len(g[s])):
            if g[s][i][1] == os:
                print(p, '*')
                break
        else:
            print(p,'.')

    v[s] = 0
    for i in range(len(g[s])):
        nbr = g[s][i][1]
        if nbr not in v.keys():
            hamiltonian_path_cycles(g,nbr,v,p+str(nbr),os)
    v.pop(s)
    

hamiltonian_path_cycles(graph,src,visited,str(src),src)

