class Node:
    def __init__(self):
        self.val = 0
        self.next = []
    def setVal(self, value):
        self.val = value
    def addNext(self, nextNode):
        self.next.append(nextNode)

class MSP:
    def __init__(self):
        
