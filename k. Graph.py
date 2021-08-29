from collections import defaultdict
graph = defaultdict(list)

def addEdge(graph,u,v):
	graph[u].append(v)

def generate_edges(graph):
	edges = []
	for node in graph:
		for neighbour in graph[node]:
			edges.append((node, neighbour))
	return edges

# declaration of graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'c','d')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'d','c')

print(generate_edges(graph))

'''output:  [('a', 'c'), ('b', 'c'), ('c', 'd'), ('c', 'a'), ('c', 'b'), ('d', 'c')]'''
