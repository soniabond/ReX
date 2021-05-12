from pythonds.basic.stack import Stack
emplyWord = 'e'


ar = "hehheldskhfkashfsfdlasjf'lasj'asfasnf'asnf;nlasfas!!!!!!!"
# этот МСП принимает слова состоящие из букв a, b с четным количеством букв a
class MSP:
    def __init__(self):
        self.sigma = ('a', 'b')
        self.states = ("sFirst", "sLast", "sEven", "sOdd")
        self.transitions = ( (self.states[0], emplyWord, self.states[2]), (self.states[2], emplyWord, self.states[1]),
                            (self.states[2], 'a', self.states[3]), (self.states[2], 'b', self.states[2]),
                            (self.states[3], 'a', self.states[2]), (self.states[3], 'b', self.states[3]))

    def accept(self, word):
# функция находит переходы их текущего состояние через заданный маркер
        def findTransition(state, letter):
            foundTransitions = []
            for trans in self.transitions:
                if trans[0] == state and  trans[1] == letter:
                    foundTransitions.append(trans)
            return foundTransitions
        if word.__len__() == 0:
            return true
        if word[0] != emplyWord:
            word = emplyWord + word
        if word[word.__len__() - 1] != emplyWord:
            word = word + emplyWord
        wStack = Stack()
        currState = "sFirst"
        numberLetters = 0
        stateLengthStack = Stack()

        for letter in word:
            foundTransitions = findTransition(currState, letter)
            if foundTransitions == []:
                if wStack.isEmpty():
                    return False
                else:
                    currState = wStack.pop()
                    currState = currState[0]
                    len = stateLengthStack.pop()
                    if len == 0:
                        numberLetters -= 1
                        len = stateLengthStack.pop() - 1
                        stateLengthStack.push(len)
                    continue
            else:
                stateLengthStack.push(foundTransitions.__len__())
                for trans in foundTransitions:
                    wStack.push(trans)
                    if trans[2] == "sLast" and numberLetters+1 == word.__len__():
                        return True
                currState = wStack.pop()
                currState = currState[2]
                numberLetters += 1
                len = stateLengthStack.pop() - 1
                stateLengthStack.push(len)
        return False



print(firstTransEnd)
msp = MSP()
# True
print(msp.accept("aabbaaaba"))
# False
print(msp.accept("a"))
# True
print(msp.accept("aba"))
# False
print(msp.accept("ac"))