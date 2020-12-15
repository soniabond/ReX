sigma = ['a', 'b', 'c', 'd']
empty = 'e'
N = ['S', 'A', 'B', 'C']
S = N[0]
P = {'S': [['A', 'a'], ['B']], 'A': [['A']], 'C': [['a'], ['b'], ['c'], ['d'], ['S']], 'B': [['d'], [empty]]}


def vanashings(sigma, N, S, P):
    vanishingTerms = []
    vanishingTermsSize = 0
    found = 1
    while True:
        for item in N:
            if item not in P:
                continue
            for following in P[item]:
                if following[0] == empty and item not in vanishingTerms:
                    vanishingTerms.append(item)
                    print(item)
                    break
                for elem in following:
                    if elem not in vanishingTerms:
                        found = 0
                        break
                if found == 1 and item not in vanishingTerms:
                    vanishingTerms.append(item)
                found = 1
        if vanishingTermsSize == len(vanishingTerms):
            break
        vanishingTermsSize = len(vanishingTerms)

    return vanishingTerms



graph = buildGraph(N, P)
print("input")
print("N:", N)
print("P:", P)
print("output")
print("Graph:", graph)
circleVertexes = circleSearch(graph)
print("Vertexes with circles", circleVertexes)
vanishingTerms = vanashings(sigma, N, S, P)