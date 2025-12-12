class BSTNode:
    """
    Represents a single node of a Binary Search Tree.
    Stores:
        key   - used for ordering
        value - optional extra data
        left  - left child
        right - right child
    """

    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    """
    Binary Search Tree supporting:

    - insert(key, value=None)
    - search(key)
    - delete(key)
    - inorder, preorder, postorder traversal (recursive)
    - inorder_iterative() using a stack

    """

    def __init__(self):
        self.root = None


    # Search

    def search(self, key):
        current = self.root
        while current:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None


    # Insert

    def insert(self, key, value=None):
        """
        Insert a key into the BST.
        Returns old value if key already exists.
        """
        if self.root is None:
            self.root = BSTNode(key, value)
            return None

        parent = None
        current = self.root

        while current:
            if key == current.key:
                old = current.value
                current.value = value
                return old

            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if key < parent.key:
            parent.left = BSTNode(key, value)
        else:
            parent.right = BSTNode(key, value)

        return None


    # Find minimum node (helper)

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node


    # Delete

    def delete(self, key):
        deleted_value = None

        def _delete(node, key):
            nonlocal deleted_value

            if node is None:
                return None

            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                deleted_value = node.value

                # Case 1 – No children
                if not node.left and not node.right:
                    return None

                # Case 2 – One child
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                # Case 3 – Two children
                successor = self._min_node(node.right)
                node.key = successor.key
                node.value = successor.value
                node.right = _delete(node.right, successor.key)

            return node

        self.root = _delete(self.root, key)
        return deleted_value


    # Traversals

    def inorder_recursive(self, visit):
        def _in(node):
            if node:
                _in(node.left)
                visit(node.key, node.value)
                _in(node.right)
        _in(self.root)

    def preorder_recursive(self, visit):
        def _pre(node):
            if node:
                visit(node.key, node.value)
                _pre(node.left)
                _pre(node.right)
        _pre(self.root)

    def postorder_recursive(self, visit):
        def _post(node):
            if node:
                _post(node.left)
                _post(node.right)
                visit(node.key, node.value)
        _post(self.root)


    # Inorder iterative

    def inorder_iterative(self, visit):
        stack = []
        current = self.root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            visit(current.key, current.value)
            current = current.right
