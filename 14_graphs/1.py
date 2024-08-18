#graph -> vertex, edge
#directed

#repersentation  -> adjancy matrix, adjancy list

#matrix -> vertex < 10,000  ->vertex 2D matrix filled with weights

#list  -> edges 
g = [(0,3,40),(0,1,10),(2,3,10),(1,2,10),(1,0,10),(2,1,10)]
n = int(input('No. of edges: '))
graph = {}
for i in range(n):
    #vertex = input()
    graph[i] = []

graph[0].append((0,3,40))
graph[0].append((0,1,10))

graph[1].append((1,0,10))
graph[1].append((1,2,10))

graph[2].append((2,3,10))
graph[2].append((2,1,10))

print(graph)

mg = {}
for i in g:
    if i[0] in mg.keys():
        mg[i[0]].append(i)
    else:
        mg[i[0]] = [i]  

print(mg)

vertex = int(input('Vertex: '))
edges = int(input('Edges: '))

ngraph = {}
print('Vertex')
for i in range(vertex):
    v = input()
    ngraph[v] = []

print('Edges')
for i in range(edges):
    ipt = input().split(' ')
    v1 = ipt[0]
    v2 = ipt[1]
    wt = int(ipt[2])

    ngraph[v1].append((v1,v2,wt))
    ngraph[v2].append((v2,v1,wt))
    

print(ngraph)
