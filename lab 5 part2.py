class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        return root

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_node = self._find_min(root.right)
            root.key = min_node.key
            root.right = self._delete_recursive(root.right, min_node.key)

        return root

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, root, result):
        if root:
            self._inorder_recursive(root.left, result)
            result.append(root.key)
            self._inorder_recursive(root.right, result)

    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, root, result):
        if root:
            result.append(root.key)
            self._preorder_recursive(root.left, result)
            self._preorder_recursive(root.right, result)

    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, root, result):
        if root:
            self._postorder_recursive(root.left, result)
            self._postorder_recursive(root.right, result)
            result.append(root.key)


if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [50, 30, 20, 40, 70, 60, 80]

    for val in values:
        bst.insert(val)

    print("Inorder traversal  :", bst.inorder())
    print("Preorder traversal :", bst.preorder())
    print("Postorder traversal:", bst.postorder())

    bst.delete(20)
    print("\nAfter deleting 20 (leaf node):")
    print("Inorder traversal  :", bst.inorder())

    bst.delete(30)
    print("\nAfter deleting 30 (node with one/two children):")
    print("Inorder traversal  :", bst.inorder())

    bst.delete(50)
    print("\nAfter deleting 50 (root node):")
    print("Inorder traversal  :", bst.inorder())