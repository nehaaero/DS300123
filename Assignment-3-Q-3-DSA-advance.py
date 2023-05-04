class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node is not None:
        print(node.value, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.value, end=" ")
        in_order_traversal(node.right)

def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=" ")

# Constructing the binary tree
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

# Perform the traversals
print("Pre-order traversal: ", end="")
pre_order_traversal(root)
print()

print("In-order traversal: ", end="")
in_order_traversal(root)
print()

print("Post-order traversal: ", end="")
post_order_traversal(root)
print()
