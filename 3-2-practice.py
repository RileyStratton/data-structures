class BST:

    class Node:

        def __init__(self, data):
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):

        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root


    def _insert(self, data, node):

        if data == node.data:
            return

        elif data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)

        elif data > node.data:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)

    def __contains__(self, data):

        return self._contains(data, self.root) 

    def _contains(self, data, node):
        # TODO - implement this method
        # Use _insert as an example
        pass

    def __iter__(self):

        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
       
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):
        # TODO - implement this method
        # Use traverse_forward as an example
        pass



# Test Code

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(7)  
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)

print(3 in tree)
print(2 in tree)
print(7 in tree)
print(6 in tree)
print(9 in tree)

print()

print ("[", end="")
for node in reversed(tree):
    print(node, end=", ")
print("]")