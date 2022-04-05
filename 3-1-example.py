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

    def __iter__(self):

        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def get_height(self):

        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)

    def _get_height(self, node):

        if node is None:
            return 0

        left_length = self._get_height(node.left)
        right_length = self._get_height(node.right)
        
        return max(left_length, right_length) + 1



# Test code

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(7)  
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)

print ("[", end="")
for node in tree:
    print(node, end=", ")
print("]")

print()

print(tree.get_height())
tree.insert(6)
print(tree.get_height())
tree.insert(12)
print(tree.get_height())