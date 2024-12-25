class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse_preorder(self):
        # Start with the current node's value
        yield self.value

        # Recursively traverse the left subtree
        if self.left:
            yield from self.left.traverse_preorder()

        # Recursively traverse the right subtree
        if self.right:
            yield from self.right.traverse_preorder()


# Construct the binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1, Node(2, Node(4), Node(5)), Node(3))

# Perform pre-order traversal
print("Pre-order Traversal:")
i = 0
for value in root.traverse_preorder():
    print("Step:" + str(i))
    i += 1
    print(value, end=" ")
