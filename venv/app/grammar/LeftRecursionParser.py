from itertools import *
import vanishings

sigma = ['a', 'b', 'c', 'd']
empty = 'e'
N = ['S', 'A', 'B', 'C']
S = N[0]
P = {'S': [['A', 'a'], ['B']], 'C': [['S', 'a', 'B'], ['a'], ['b'], ['c'], ['d']], 'A': [['A', 'c'], ['a']],  'B': [[empty], ['d']]}

# for i in product('10', repeat=4):
#     print(i, end=' ')

def generateNewTerm(lastTerm):
    term = chr(ord(lastTerm)+1)
    if term == S:
        term = chr(ord(lastTerm) + 2)
    return term

def findVanishingsInRule(rule, allVanishing):
    vanishs = []
    for item in allVanishing:
        if item in rule:
            vanishs.append(item)
    return vanishs


def deleteAllVanishings(sigma, N, S, P):
    allVanishings = vanishings.vanashings(sigma, N, S, P)
    for item in P:
        result = []
        for rule in P[item]:
            if not rule.__eq__([empty]):
               result.append(rule)
        P[item] = result
    for item in P:
        newRules = []
        for rule in P[item]:
            listVanishInRule = findVanishingsInRule(rule, allVanishings)
            if listVanishInRule == []:
                newRules.append(rule)
                continue
            products = product('01', repeat=listVanishInRule.__len__())

            for prod in products:
                newRule = []
                i = 0
                for term in rule:
                    if term not in listVanishInRule:
                        newRule.append(term)
                    elif term in listVanishInRule:
                        if prod[i] == '1':
                            newRule.append(term)
                        i += 1
                if newRule == []:
                    continue
                newRules.append(newRule)
        P[item] = newRules
    print(P)
    return P


def deleteStraightLestRecursion(term, P, N):
    newTerm = generateNewTerm(N[len(N)-1])
    outputsToAppend = []
    newOutputs = []
    for rule in P[term]:
        if rule[0] != term:
            print(rule)
            outputsToAppend.append(rule)
            continue
        if rule[0] == term:
            newRule = rule.copy()
            newRule.pop(0)
            newRule.append(newTerm)
            newOutputs.append(newRule)
    if newOutputs == []:
        return P
    P[term] = outputsToAppend
    for rule in P[term]:
        rule.append(newTerm)
    newOutputs.append([empty])
    P[newTerm] = newOutputs
    N.append(newTerm)
    print(P)
    return P





newP = deleteAllVanishings(sigma, N, S, P)
deleteStraightLestRecursion('A', newP, N)
