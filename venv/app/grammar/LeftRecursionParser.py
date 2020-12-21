from itertools import *
import vanishings
import LeftRecursion
from queue import Queue
from pythonds.basic.stack import Stack
import Nonterminals

sigma = ['a', 'b', 'c', 'd']
N = ['S', 'A', 'B', 'C', 'D', 'F']
S = N[0]
P = {'S': [['A', 'a'], ['B', 'b'], ['C']], 'A': [['S', 'C']], 'C': [['a'], ['b'], ['c'], ['d']], 'D': [['C', 'a'], ['F']], 'F': [['B']]}
empty = 'e'

# sigma = ['*', '|', 'c', 'n', ',']
# empty = 'e'
# N = ['S', 'A', 'P', 'C', 'D']
# S = N[0]
# P = {'S': [['S', '|', 'S'], ['A']], 'A': [['A', ',', 'A'], ['P']],  'P': [['P', '*'], ['c'], ['n']]}
end = '-'


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


def deleteAllVanishings():
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
                if newRule not in newRules:
                    newRules.append(newRule)
        P[item] = newRules
    #print(P)
    return P, N


def deleteStraightLestRecursion(term):
    newTerm = generateNewTerm(N[len(N)-1])
    outputsToAppend = []
    newOutputs = []
    for rule in P[term]:
        if rule[0] != term:
            #print(rule)
            outputsToAppend.append(rule)
            continue
        if rule[0] == term:
            newRule = rule.copy()
            newRule.pop(0)
            if newRule != []:
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
    #print(P)
    return P, N


def eraseRightTerm(term):
    for nonterminal in P:
        newOutputs = []
        for rule in P[nonterminal]:
            if rule[0]!= term:
                newOutputs.append(rule)
                continue
            if rule[0] == term:
                for output in P[term]:
                    newRule = output + rule[1:]
                    newOutputs.append(newRule)
        P[nonterminal] = newOutputs
    return P


def deleteRecForAll():
    while True:
        for term in list(P):
            deleteStraightLestRecursion(term)
            eraseRightTerm(term)
        if LeftRecursion.diagnoseRecurison(N, P) == []:
            break


def parse(word, terms):
    if terms == [] and len(word)==1:
        return True
    if terms == []:
        return False
    firstTerm = terms.pop()
    if firstTerm == empty:
        if len(terms) != 0:
            firstTerm = terms.pop()
        elif len(terms) == 0 and len(word)>0:
            return False

    if len(word) == 1 and len(terms) == 0:
        if firstTerm == empty:
           return True
        return False
    if firstTerm in sigma and word[len(word)-1] != firstTerm:
        return False
    if firstTerm in sigma and word[len(word)-1] == firstTerm:
        word.pop()
        flag = parse(word.copy(), terms.copy())
        return flag
    for term in P[firstTerm]:
        count = term.__len__()
        if count == 0:
            terms.append(term[0])
        else:
            for i in range(count-1, -1, -1):
                terms.append(term[i])
        flag = parse(word.copy(), terms.copy())
        if flag == True:
            return True
        if count == 0:
            terms.pop()
        else:
            for i in range(count):
                terms.pop()
    return False



print("P in the beginning: ", P)
print("N in the beginning: ", N)
P, N = Nonterminals.deleteExtraTerminals(sigma, N, S, P)
deleteAllVanishings()
print("P after delete vanish ", P)
print("N after delete vanish ", N)
deleteRecForAll()
print("P with all recursion deleted:", P)
print("new set of N ", N)
print("----------------------------------------------------------------")
word = list()
word.append('b')
word.append('b')
word.append('a')
word.append(end)
word.reverse()
terms = ['S']
wordOutput = word.copy()
wordOutput.reverse()
print("word: ", wordOutput, "is deducible: ", parse(word, terms))
print("----------------------------------------------------------------")
word = list()
word.append('b')
word.append('b')
word.append('b')
word.append(end)
word.reverse()
terms = ['S']
wordOutput = word.copy()
wordOutput.reverse()
print("word: ", wordOutput, "is deducible: ", parse(word, terms))
print("----------------------------------------------------------------")
word = list()
word.append('c')
word.append('b')
word.append('a')
word.append(end)
word.reverse()
terms = ['S']
wordOutput = word.copy()
wordOutput.reverse()
print("word: ", wordOutput, "is deducible: ", parse(word, terms))


# EXAMPLE OUTPUT
# P in the beginning:  {'S': [['A', 'a'], ['B', 'b'], ['C']], 'A': [['S', 'C']], 'C': [['a'], ['b'], ['c'], ['d']], 'D': [['C', 'a'], ['F']], 'F': [['B']]}
# N in the beginning:  ['S', 'A', 'B', 'C', 'D', 'F']
# P after delete vanish  {'S': [['A', 'a'], ['C']], 'A': [['S', 'C']], 'C': [['a'], ['b'], ['c'], ['d']]}
# N after delete vanish  ['S', 'A', 'C']
# P with all recursion deleted: {'S': [['a', 'C', 'D', 'a'], ['b', 'C', 'D', 'a'], ['c', 'C', 'D', 'a'], ['d', 'C', 'D', 'a'], ['a'], ['b'], ['c'], ['d']], 'A': [['a', 'C', 'D'], ['b', 'C', 'D'], ['c', 'C', 'D'], ['d', 'C', 'D']], 'C': [['a'], ['b'], ['c'], ['d']], 'D': [['a', 'C', 'D'], ['e']]}
# new set of N  ['S', 'A', 'C', 'D']
# ----------------------------------------------------------------
# word:  ['b', 'b', 'a', '-'] is deducible:  True
# ----------------------------------------------------------------
# word:  ['b', 'b', 'b', '-'] is deducible:  False
# ----------------------------------------------------------------
# word:  ['c', 'b', 'a', '-'] is deducible:  True
#
# Process finished with exit code 0

