import sys
from operator import attrgetter


class Node:

    def __init__(self):
        self.name = ''
        self.weight = 0
        self.code = ''

    def initSet(self, name, weight):
        self.name = name
        self.weight = weight

    def setRoot(self, root):
        self.root = root

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def addCode(self, code):
        self.code = code + self.code


def buildHuffTree(tree):

    def setHuffcode(root, code):
        root.addCode(code)

        try:
            setHuffcode(root.left, code)
        except:
            pass
        try:
            setHuffcode(root.right, code)
        except:
            pass

        return root

#    for i in range(10):
#        setHuffcode(tree[i], str(i))

    while len(tree) >= 2:
        sorted(tree, key=attrgetter('weight'))
        newNode = Node()
        name = tree[0].name + tree[1].name
        weight = tree[0].weight + tree[1].weight
        newNode.initSet(name, weight)
        tree[0].setRoot(newNode)
        tree[1].setRoot(newNode)
        setHuffcode(tree[0], '1')
        setHuffcode(tree[1], '0')
        newNode.setLeft = tree[0]
        newNode.setRight = tree[1]
        tree.pop(1)
        tree.pop(0)
        tree.append(newNode)


def main():
    weight = input()
    decode = input()
    weight = weight.split()

    Tree = [Node() for i in range(len(weight))]

    for i, T in enumerate(Tree):
        T.initSet(str(i), float(weight[i]))

    buildHuffTree(Tree)


if __name__ == '__main__':
    main()
    sys.exit()
