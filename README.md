# Binary Search Tree Library

A robust, pure-Python implementation of a Binary Search Tree (BST) supporting key-value storage. This project 
demonstrates core data structure algorithms including recursive insertion, deletion, 
and multiple traversal methods.

## Project Structure

```text
Binary_Search_Tree/
├── bst.py                 # The core library class
├── word_frequency_demo.py # A demo application (Word Counter)
├── test_bst.py            # Unit tests ensuring stability
└── README.md              # Project documentation

```

## Features

**Key-Value Storage:** Operates like a Map/Dictionary, storing values associated with sortable keys

**CRUD Operations:** 
* Insert: Add nodes recursively
* Search: Find values efficiently O(log n).
* Delete: Remove nodes while maintaining tree integrity (handles leaf, single-child, and two-child cases).

**Traversals:**
* Recursive: Inorder, Preorder, Postorder.
* Iterative: Inorder traversal using a stack.

## Start

**Installation:**
No special installation is required. Simply download the `bst.py` file and place it in your project directory.
````
**Basic Usage:**

from bst import BST

**Initialize the tree**

 tree = BST()
     
**Insert data (Key, Value)**

 tree.insert(50, "Root Node")
 tree.insert(30, "Left Child")
 tree.insert(70, "Right Child")

**Search for data**

 result = tree.search(30)
 print(f"Found: {result}")  # Output: Found: Left Child

**Delete data**

 tree.delete(70)
 print(tree.search(70))     # Output: None
````

## Demo Application: Word Frequency Counter

The included `word_frequency_demo.py` demonstrates a real-world application of this library.
It parses a text string, uses the BST to track how often each word appears, and prints
the results alphabetically.

**To run the demo:**

```sh
  python word_frequency_demo.py
```

## Running Tests 

This project includes a suite of unit tests `test_bst.p` to verify the stability
of insertions, deletions, and edge cases.

## Core Algorithms
This library implements the following standard BST algorithms:
1. **Insertion:** Recursively finds the correct position based on `key < node.key` logic.
2. **Inorder Traversal:** Visits nodes in `Left -> Root -> Right` order to retrieve sorted data.
3. **Deletion:** When deleting a node with two children, the algorithm finds the Inorder Successor,
   replaces the target node's data with the successor's data, and then deletes the original successor node.