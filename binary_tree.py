"""
Binary tree is a non linear data structure where it has a root node
and that root node can have multiple children nodes associated with it.
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def show(self):
        if self.left:
            self.left.show()
        print self.data
        if self.right:
            self.right.show()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.show()