#!/usr/bin/env python3
import re
from bst import BST

def tokenize(text: str) -> list[str]:

    return re.findall(r"[A-Za-z0-9_']+", text.lower())


def build_frequency_bst(words: list[str]) -> BST:
    """
    Build a BST where:
        key   = word
        value = count (int)
    """
    tree = BST()

    for word in words:
        current_count = tree.search(word)
        if current_count is None:
            tree.insert(word, 1)
        else:
            tree.insert(word, current_count + 1)

    return tree


def print_frequencies(tree: BST) -> None:


    if tree.root is None:
        print("No words to display (tree is empty).")
        return

    def visit(word, count):
        print(f"{word}: {count}")

    tree.inorder_recursive(visit)


def main() -> None:
    text = "Hello World, hello everyone, I came to thank all of you for your hardwork"
    words = tokenize(text)

    if not words:
        print("No words found in input.")
        return

    tree = build_frequency_bst(words)
    print_frequencies(tree)


if __name__ == "__main__":

    main()
