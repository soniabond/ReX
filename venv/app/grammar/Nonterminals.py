# sigma = ['a', 'b', 'c', 'd']
# N = ['S', 'A', 'B', 'C', 'D', 'F']
# S = N[0]
# P = {'S': [['A', 'a'], ['B', 'b']], 'A': [['C']], 'C': [['a'], ['b'], ['c'], ['d']], 'D': [['C', 'a'], ['F']], 'F': [['B']]}


def alives(sigma, N, S, P):
    newP = dict()
    newN = []
    aliveTerminals = []
    found = 1
    aliveTerminalSize = 0
    while True:
        for item in N:
            if item not in P:
                continue
            for followings in P[item]:
                for elem in followings:
                    if elem not in sigma and elem not in aliveTerminals:
                        found = 0
                        break
                if found ==1:
                    if item in N and item not in aliveTerminals:
                        aliveTerminals.append(item)
                        break
                found = 1
        for item in N:
            if item not in P:
                newN.append(item)
                continue
            if item not in aliveTerminals:
                continue
            else:
                newP[item] = P[item]
                newN.append(item)
        if aliveTerminalSize == len(aliveTerminals):
            break
        aliveTerminalSize = len(aliveTerminals)

    for key in newP:
        for i in range(len(newP[key])):
            if i>= len(newP[key]):
                break
            for j in range(len(newP[key][i])):
                if newP[key][i][j] not in aliveTerminals and newP[key][i][j] not in sigma:
                    newP[key].remove(newP[key][i])
                    i+=1
                    break


    return newP, aliveTerminals



def reachables(sigma, N, S, P):
    newP = dict()
    # newN = [S]
    reachableTerminals = [S]
    found = 1
    reachableTerminalSize = 1
    newP[S] = P[S]
    while True:
        for Pkey in P:
            for Rterm in reachableTerminals:
                if Pkey == Rterm:
                    for followings in P[Rterm]:
                        for elem in followings:
                            if elem not in reachableTerminals and elem in N:
                                reachableTerminals.append(elem)
                                newP[elem] = P[elem]

        if reachableTerminalSize == len(reachableTerminals):
            break
        reachableTerminalSize = len(reachableTerminals)

    for key in newP:
        for i in range(len(newP[key])):
            for j in range(len(newP[key][i])):
                if newP[key][i][j] not in reachableTerminals and newP[key][i][j] not in sigma:
                    newP[key].remove(newP[key][i])
                    i+=1
                    break

    return newP, reachableTerminals


def deleteExtraTerminals(sigma, N, S, P):
    newP, newN = alives(sigma, N, S, P)
    newP, newN = reachables(sigma, newN, S, newP)
    return newP, newN


# deleteExtraTerminals(sigma, N, S, P)

# EXAMPLE OF OUTPUT
# before
# sigma = ['a', 'b', 'c', 'd']
# S = 'S'
# N: ['S', 'A', 'B', 'C', 'D', 'F']
# P: {'S': [['A', 'a'], ['B', 'b']], 'A': [['C']], 'C': [['a'], ['b'], ['c'], ['d']], 'D': [['C', 'a'], ['F']], 'F': [['B']]}
# after deleting not alive terminals
# N: ['C', 'D', 'A', 'S']
# P: {'C': [['a'], ['b'], ['c'], ['d']], 'D': [['C', 'a']], 'A': [['C']], 'S': [['A', 'a']]}
# and after deleting unreachable terminals
# N: ['S', 'A', 'C']
# P: {'S': [['A', 'a']], 'A': [['C']], 'C': [['a'], ['b'], ['c'], ['d']]}
#
# Process finished with exit code 0

