class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
        else:
            self._add_node(node, self.root)

    def _add_node(self, node, current_node):
        if node.value < current_node.value:
            if current_node.left is None:
                current_node.left = node
            else:
                self._add_node(node, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = node
            else:
                self._add_node(node, current_node.right)

    def print_tree(self, traversal_type):
        if traversal_type == "inorder":
            self._inorder_traversal(self.root)
        elif traversal_type == "preorder":
            self._preorder_traversal(self.root)
        elif traversal_type == "postorder":
            self._postorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.value, end=" ")
            self._inorder_traversal(node.right)

    def _preorder_traversal(self, node):
        if node:
            print(node.value, end=" ")
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def _postorder_traversal(self, node):
        if node:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            print(node.value, end=" ")

tree = BinaryTree()
tree.add_node(5)
tree.add_node(3)
tree.add_node(7)
tree.add_node(1)
tree.add_node(4)
tree.add_node(6)
tree.add_node(8)

tree.print_tree("inorder")