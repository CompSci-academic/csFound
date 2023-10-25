class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def insert(self, value):
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left:
                self._insert_recursive(current.left, value)
            else:
                current.left = TreeNode(value)
        elif value > current.value:
            if current.right:
                self._insert_recursive(current.right, value)
            else:
                current.right = TreeNode(value)
        else:
            # Value already exists, no duplicates allowed
            pass

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current:
            if current.value == value:
                return True
            if value < current.value:
                return self._search_recursive(current.left, value)
            else:
                return self._search_recursive(current.right, value)
        return False

# Create a binary tree with a root node value of 5
tree = BinaryTree(5)

# Insert values into the tree
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Search for a value in the tree
value_to_search = 4
if tree.search(value_to_search):
    print(f"Found {value_to_search} in the tree.")
else:
    print(f"{value_to_search} not found in the tree.")
