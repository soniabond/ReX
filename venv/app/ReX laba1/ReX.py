from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

class ReX:


#creating tree using build in structure BinaryTree
    def __init__(self, fpexp):
        fplist = fpexp.split()
        pStack = Stack()
        eTree = BinaryTree('')
        pStack.push(eTree)
        currentTree = eTree
        flag = 0
        for i in range(len(fplist)):
            item = fplist[i]
            #if item == ( then moving to the left child
            if item == '(':
                currentTree.insertLeft('')
                pStack.push(currentTree)
                currentTree = currentTree.getLeftChild()
            #if item is alpha then put value to the leaf and go back to previous node
            elif item not in [',', '|', '*', ')']:
                currentTree.setRootVal(item)
                parent = pStack.pop()
                currentTree = parent
            elif flag == 1 and item == ' ' :
                currentTree.setRootVal(item)
                parent = pStack.pop()
                currentTree = parent
                flag = 0
            #if item is , | or * then put the value into node and move to right child
            elif item in [',', '|', '*']:
                currentTree.setRootVal(item)
                if item == '*':
                    fplist.insert(i+1, '')
                    flag = 1
                currentTree.insertRight('')
                pStack.push(currentTree)
                currentTree = currentTree.getRightChild()
            #if item == ) then move back to previous node
            elif item == ')':
                currentTree = pStack.pop()
            else:
                raise ValueError
        self.tree = eTree;


    def __str__(self):
        strTree = ""

        #retting the row tree by crawl depth from left to right
        def printTree(root):
            if root == None:
                return
            nonlocal strTree
            strTree += root.getRootVal()
            printTree(root.getLeftChild())
            printTree(root.getRightChild())

        printTree(self.tree)
        strList = []
        move = 0
        starFlag = 0
        # put parenthesis on right places
        for i in range(len(strTree)):
            strList.insert(i+move, strTree[i])


            if strTree[i] in ['|', '*', ',']:
                strList.insert(i+move, " ( ")
                move += 1
            elif i<len(strTree)-1 and strTree[i+1].isalpha():
                strList.insert(i + move, " ( ")
                move += 1
            elif strTree[i].isalpha():
                strList.insert(i+move+1, " ) ")
                move += 1

        strList.insert(len(strList), " ) ")
        return "".join(strList)








arr = " ( ( ( a | b ) , ( c | d ) ) * ) "
arr1 = "( ( a * ) , ( b * ) )"
arr2 = "( a , b )"
splt = arr.split()

splt.insert(1, "|")

print("SOME TEST CASES\n")
print("regex 1 =", arr)
print("tree created. row representation of tree:")
rex = ReX(arr)
# ( * ( , ( | ( ab )  ( | ( cd )  )
print(rex)

print("____________________________________________")
print("regex 2 =", arr1)
print("tree created. row representation of tree:")
rex1 = ReX(arr1)
print(rex1)
# ( , ( *a )  ( *b )  )

print("____________________________________________")
print("regex 3 =", arr2)
print("tree created. row representation of tree:")
rex2 = ReX(arr2)
# ( , ( ab )  )
print(rex2)



