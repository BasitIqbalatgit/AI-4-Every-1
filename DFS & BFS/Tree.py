class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None  # Initialize an empty tree

    def insert(self, value):

        def _insert_rec(node, value):
            if not node:
                return TreeNode(value)  # Create a new node if current node is None
            if value < node.value:
                node.left = _insert_rec(node.left, value)  # Insert into the left subtree
            elif value > node.value:
                node.right = _insert_rec(node.right, value)  # Insert into the right subtree
            return node

        # Call the helper function to insert the value
        self.root = _insert_rec(self.root, value)

    def inorder_traversal(self):
        # Helper function to perform inorder traversal
        def _inorder_rec(node):
            if node:
                _inorder_rec(node.left)  # Visit left subtree
                print(node.value, end=' ')  # Visit current node
                _inorder_rec(node.right)  # Visit right subtree

        # Call the helper function to start inorder traversal from the root
        _inorder_rec(self.root)
        print()  # Move to the next line after traversal
