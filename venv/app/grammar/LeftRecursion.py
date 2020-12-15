sigma = ['a', 'b', 'c', 'd']
N = ['S', 'A', 'B', 'C']
S = N[0]
P = {'S': [['A', 'a'], ['B', 'b']], 'A': [['C'], ['A']], 'C': [['a'], ['b'], ['c'], ['d'], ['S', 'a']], 'B': [['d']]}


def buildGraph(N, P):
    graph = dict()
    for key in P:
        graph[key] = []
        for i in range(len(P[key])):
            if P[key][i][0] in N:
                graph[key].append(P[key][i][0])

    return graph


def circleSearch(graph):
    circleVertexes = []
    visited = []

    def dfs(vertex):
        nonlocal visited
        visited.append(vertex)
        nonlocal graph
        for v in graph[vertex]:
            if v not in visited:
                dfs(v)
            if v in visited:
                if vertex not in circleVertexes:
                    circleVertexes.append(vertex)

    dfs(N[0])
    return circleVertexes



graph = buildGraph(N, P)
print("input")
print("N:", N)
print("P:", P)
print("output")
print("Graph:", graph)
circleVertexes = circleSearch(graph)
print("Vertexes with circles", circleVertexes)

# EXAMPLE OF CHECHENG LEFT RECURSION
# input
# N: ['S', 'A', 'B', 'C']
# P: {'S': [['A', 'a'], ['B', 'b']], 'A': [['C'], ['A']], 'C': [['a'], ['b'], ['c'], ['d'], ['S', 'a']], 'B': [['d']]}
# output
# Graph: {'S': ['A', 'B'], 'A': ['C', 'A'], 'C': ['S'], 'B': []}
# Vertexes with circles ['C', 'A', 'S']
#
# Process finished with exit code 0