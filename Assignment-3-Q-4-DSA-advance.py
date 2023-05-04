class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_leaves(root):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        print(root.data)
    
    if root.left:
        print_leaves(root.left)
    
    if root.right:
        print_leaves(root.right)

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Call the print_leaves function
print("Leaves of the binary tree:")
print_leaves(root)