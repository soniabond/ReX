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
                if secondTrans == None:
                    transitions.insert(counter, [startState, token, lastState]);
                    firstTransStart = transitions[counter]
                    firstTransEnd = transitions[counter]
                    counter += 1
                else:
                    transitions.insert(counter, [startState, token, lastState]);
                    secondTransStart = transitions[counter]
                    secondTransEnd = transitions[counter]
                    counter += 1
            if token == ',':
                newEndFirst = "s"+str(self.states.__len__())
                self.states.append(newEndFirst)
                newStartSecond = "s" + str(self.states.__len__())
                self.states.append(newStartSecond)
                firstTransEnd[2]=newEndFirst
                secondTransStart[0]=newStartSecond
                transitions.insert(counter, [newEndFirst, emptyWord, newStartSecond]);
                counter+=1
                firstTransEnd = secondTransEnd
                secondTransEnd = None
                secondTransStart = None

            if token == '|':
                newStartFirst = "s" + str(self.states.__len__())
                self.states.append(newStartFirst)
                newEndFirst = "s" + str(self.states.__len__())
                self.states.append(newEndFirst)
                newStartSecond = "s" + str(self.states.__len__())
                self.states.append(newStartSecond)
                newEndSecond = "s" + str(self.states.__len__())
                self.states.append(newEndSecond)
                transitions.insert(counter, [startState, emptyWord, newStartFirst]);
                firstTransStart[0] = newStartFirst
                counter+=1
                firstTransStart = transitions[counter-1]
                transitions.insert(counter, [startState, emptyWord, newStartSecond]);
                secondTransStart = None
                counter += 1
                transitions.insert(counter, [startState, emptyWord, newStartFirst]);
                firstTransStart[0] = newStartFirst
                counter += 1










