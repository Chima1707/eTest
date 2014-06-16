
""" Question 1
Depth first tree traversal in Python
Discuss an algorithm to traverse a tree, depth first.
"""

class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children


def visitTreeNode(node):
    whatToDo(node)
    if node.children:
        for child in node.children:
            visitTreeNode(child)


def printAllElements(node):
    visitTreeNode(node)

def whatToDo(x):
    print x.name


x=Node("x",None)
y=Node("y",None)
params=[x,y]
z=Node("z", params)
printAllElements(z)
