startState = "sFirst"
lastState = "sLast"
emptyWord = 'e'
class ReX2LTS:
    def __init__(self, btree):
        print(btree)
        transitions = []
        self.states = [startState, lastState]
        strTree = ""
        def getNextTreeNode(root):
            if root == None:
                return
            getNextTreeNode(root.getLeftChild())
            getNextTreeNode(root.getRightChild())
            nonlocal strTree
            if(root.getRightChild!=' '):
                strTree += root.getRootVal()
        counter = 0
        getNextTreeNode(btree)
        firstTransStart = None
        firstTransEnd = None
        secondTransStart = None
        secondTransEnd = None
        thirdTransStart = None
        thirdTransEnd = None
        for token in strTree:
            if token.isalpha():
                if firstTransStart == None:
                    transitions.insert(counter, [startState, token, lastState]);
                    firstTransStart = transitions[counter]
                    firstTransEnd = transitions[counter]
                    counter += 1
                elif secondTransStart == None:
                    transitions.insert(counter, [startState, token, lastState]);
                    secondTransStart = transitions[counter]
                    secondTransEnd = transitions[counter]
                    counter += 1
                else:
                    transitions.insert(counter, [startState, token, lastState]);
                    thirdTransStart = transitions[counter]
                    thirdTransEnd = transitions[counter]
                    counter += 1
            if token == ',':
                newEndFirst = "s"+str(self.states.__len__())
                self.states.append(newEndFirst)
                newStartSecond = "s" + str(self.states.__len__())
                self.states.append(newStartSecond)
                if thirdTransStart == None:
                    firstTransEnd[2]=newEndFirst
                    secondTransStart[0]=newStartSecond
                    transitions.insert(counter, [newEndFirst, emptyWord, newStartSecond]);
                    counter+=1
                    firstTransEnd = secondTransEnd
                    secondTransEnd = None
                    secondTransStart = None
                else:
                    secondTransEnd[2] = newEndFirst
                    thirdTransStart[0] = newStartSecond
                    transitions.insert(counter, [newEndFirst, emptyWord, newStartSecond]);
                    counter += 1
                    secondTransEnd = thirdTransEnd
                    thirdTransEnd = None
                    thirdTransStart = None

            if token == '|':
                newStartFirst = "s" + str(self.states.__len__())
                self.states.append(newStartFirst)
                newEndFirst = "s" + str(self.states.__len__())
                self.states.append(newEndFirst)
                newStartSecond = "s" + str(self.states.__len__())
                self.states.append(newStartSecond)
                newEndSecond = "s" + str(self.states.__len__())
                self.states.append(newEndSecond)
                if thirdTransStart == None:
                    transitions.insert(counter, [startState, emptyWord, newStartFirst]);
                    firstTransStart[0] = newStartFirst
                    firstTransStart = transitions[counter]
                    counter += 1
                    transitions.insert(counter, [startState, emptyWord, newStartSecond]);
                    secondTransStart[0] = newStartSecond
                    secondTransStart = None
                    counter += 1
                    transitions.insert(counter, [newEndFirst, emptyWord, lastState]);
                    firstTransEnd[2] = newEndFirst
                    firstTransEnd = transitions[counter]
                    counter += 1
                    transitions.insert(counter, [newEndSecond, emptyWord, lastState]);
                    secondTransEnd[2] = newEndSecond
                    secondTransEnd = None
                    counter += 1
                else:
                    transitions.insert(counter, [startState, emptyWord, newStartFirst]);
                    secondTransStart[0] = newStartFirst
                    secondTransStart = transitions[counter]
                    counter += 1
                    transitions.insert(counter, [startState, emptyWord, newStartSecond]);
                    thirdTransStart[0] = newStartSecond
                    thirdTransStart = None
                    counter += 1
                    transitions.insert(counter, [newEndFirst, emptyWord, lastState]);
                    secondTransEnd[2] = newEndFirst
                    secondTransEnd = transitions[counter]
                    counter += 1
                    transitions.insert(counter, [newEndSecond, emptyWord, lastState]);
                    thirdTransEnd[2] = newEndSecond
                    thirdTransEnd = None
                    counter += 1

            if token == '*':
                newStart = "s" + str(self.states.__len__())
                self.states.append(newStart)
                newEnd = "s" + str(self.states.__len__())
                self.states.append(newEnd)
                transitions.insert(counter, [newStart, emptyWord, newEnd]);
                counter+=1
                transitions.insert(counter, [newEnd, emptyWord, newStart]);
                counter+=1
                if thirdTransStart != None:
                    transitions.insert(counter, [startState, emptyWord, newStart]);
                    thirdTransStart[0]=newStart
                    thirdTransStart = transitions[counter]
                    counter+=1
                    transitions.insert(counter, [newEnd, emptyWord, lastState]);
                    thirdTransEnd[2] = newEnd
                    thirdTransEnd = transitions[counter]
                    counter += 1
                elif secondTransStart != None:
                    transitions.insert(counter, [startState, emptyWord, newStart]);
                    secondTransStart[0]=newStart
                    secondTransStart = transitions[counter]
                    counter+=1
                    transitions.insert(counter, [newEnd, emptyWord, lastState]);
                    secondTransEnd[2] = newEnd
                    secondTransEnd = transitions[counter]
                    counter += 1
                else:
                    transitions.insert(counter, [startState, emptyWord, newStart]);
                    firstTransStart[0]=newStart
                    firstTransStart = transitions[counter]
                    counter+=1
                    transitions.insert(counter, [newEnd, emptyWord, lastState]);
                    firstTransEnd[2] = newEnd
                    firstTransEnd = transitions[counter]
                    counter += 1
        self.transitions = transitions;

    def printTransitions(self):
        for item in self.transitions:
            print(item)









