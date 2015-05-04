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


def setHuffcode(root, code):
    root.addCode(code)

    try:
        setHuffcode(root.left, '1')
    except:
        pass
    try:
        setHuffcode(root.right, '0')
    except:
        pass
