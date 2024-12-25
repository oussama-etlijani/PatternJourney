class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right  # Right child of the current node
        self.left = left  # Left child of the current node
        self.value = value  # Value stored in the current node
        self.parent = None  # Parent node (for traversal)

        # Set parent for left and right children if they exist
        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def __iter__(self):
        # Returns an in-order iterator for the binary tree
        return InOrderIterator(self)


class InOrderIterator:
    def __init__(self, root):
        self.root = self.current = root  # Start from the root
        self.yielded_start = False  # Flag to track if iteration has started

        # Move to the leftmost node to start in-order traversal
        while self.current.left:
            self.current = self.current.left

    def __next__(self):
        # First iteration: yield the leftmost node
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        # If there's a right child, move to it and then to its leftmost descendant
        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            # Move up to the parent until the current node is not a right child
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p  # Move to the parent
            if self.current:
                return self.current  # Return the parent if it exists
            else:
                raise StopIteration  # End of traversal


def traverse_in_order(root):
    # Generator for recursive in-order traversal
    def traverse(current):
        if current.left:
            # Recursively traverse the left subtree
            for left in traverse(current.left):
                yield left
        yield current  # Yield the current node
        if current.right:
            # Recursively traverse the right subtree
            for right in traverse(current.right):
                yield right

    # Start the traversal from the root node
    for node in traverse(root):
        yield node


if __name__ == "__main__":
    # Binary Tree Structure:
    #      1
    #     / \
    #    2   3
    #
    # In-order traversal:   2, 1, 3
    # Pre-order traversal:  1, 2, 3
    # Post-order traversal: 2, 3, 1

    # Create the binary tree
    root = Node(1, Node(2), Node(3))

    # Use the iterator for in-order traversal
    it = iter(root)

    # Fetch the first three values using the iterator
    print([next(it).value for x in range(3)])  # Output: [2, 1, 3]

    # Iterate over the tree nodes using the in-order iterator
    for x in root:
        print(x.value)  # Output: 2, 1, 3

    # Recursive in-order traversal using generator
    for y in traverse_in_order(root):
        print(y.value)  # Output: 2, 1, 3
