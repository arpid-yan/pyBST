import unittest
from bst import BST


class TestBST(unittest.TestCase):

    def test_insert_search(self):
        tree = BST()
        tree.insert(50, "root")
        tree.insert(30, "left")
        tree.insert(70, "right")

        self.assertEqual(tree.search(50), "root")
        self.assertEqual(tree.search(30), "left")
        self.assertEqual(tree.search(70), "right")
        self.assertIsNone(tree.search(100))

    def test_replace_value(self):
        tree = BST()
        tree.insert(10, "A")
        old = tree.insert(10, "B")  # replace
        self.assertEqual(old, "A")
        self.assertEqual(tree.search(10), "B")

    def test_delete_leaf(self):
        tree = BST()
        tree.insert(20, "v20")
        tree.insert(10, "v10")
        tree.insert(30, "v30")

        removed = tree.delete(10)
        self.assertEqual(removed, "v10")
        self.assertIsNone(tree.search(10))

    def test_delete_one_child(self):
        tree = BST()
        tree.insert(10, "v10")
        tree.insert(5, "v5")
        tree.insert(1, "v1")  # only left child of 5

        tree.delete(5)
        self.assertIsNone(tree.search(5))
        # FIXED: Explicitly check that 1 still exists
        self.assertEqual(tree.search(1), "v1")

    def test_delete_two_children(self):
        tree = BST()
        tree.insert(50, "v50")
        tree.insert(30, "v30")
        tree.insert(70, "v70")
        tree.insert(60, "v60")  # Left child of 70
        tree.insert(80, "v80")  # Right child of 70

        tree.delete(70)  # Should be replaced by 80 (min of right subtree)

        self.assertIsNone(tree.search(70))  # 70 should be gone
        self.assertEqual(tree.search(60), "v60")  # 60 must still exist
        self.assertEqual(tree.search(80), "v80")  # 80 must still exist (moved up)


if __name__ == '__main__':
    unittest.main()