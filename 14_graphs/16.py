#Topological Sort

vertex = int(input('Vertex: '))
edges = int(input('Edges: '))

def graph(v,e):
    graph = {}
    for i in range(v):
        #vertex = input()
        graph[i] = []
    
    print('Input for edges: ')
    for i in range(e):
        ipt = input().split(' ')
        v1 = int(ipt[0])
        v2 = int(ipt[1])
        wt = int(ipt[2])

        graph[v1].append((v1,v2,wt))

    return graph

graph = graph(vertex,edges)
print(graph)

def topological_sort(graph):
    visited = [False for i in range(len(graph))]
    stack = []
    for i in graph.keys():
        if visited[i] == False:
            tree(graph,i,visited,stack)
    while stack:
        print(stack.pop())
        
def tree(g,s,v,st):
    v[s] = True
    for i in range(len(g[s])):
        nbr = g[s][i][1]
        if v[nbr] == False:
            tree(g,nbr,v,st)
    st.append(s)
    
topological_sort(graph)
