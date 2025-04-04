<<<<<<< HEAD
# Data Structures and Algorithms Solutions

This repository contains solutions for various Data Structures and Algorithms problems from LeetCode.

## Problems Solved

### 1. Reverse Linked List (LeetCode #206)
Given the head of a singly linked list, reverse the list, and return the reversed list.

#### Solution Approach
The solution uses an iterative approach to reverse the linked list:
1. Initialize a `prev` pointer as `None` (this will be the new head of the reversed list)
2. Keep track of the current node
3. For each node:
   - Store the next node temporarily
   - Reverse the link by pointing current node to previous node
   - Move the previous and current pointers forward
4. Return the new head (which will be the last node of the original list)

#### Time Complexity
- O(n) where n is the number of nodes in the linked list

#### Space Complexity
- O(1) as we only use a constant amount of extra space

#### Example
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1

### 2. Remove Nth Node From End of List (LeetCode #19)
Given the head of a linked list, remove the nth node from the end of the list and return its head.

#### Solution Approach
The solution uses the two-pointer technique:
1. Create a dummy node to handle edge cases
2. Initialize two pointers (first and second) at the dummy node
3. Move the first pointer n+1 steps ahead
4. Move both pointers until the first pointer reaches the end
5. Remove the nth node by updating the second pointer's next reference

#### Time Complexity
- O(n) where n is the number of nodes in the linked list

#### Space Complexity
- O(1) as we only use a constant amount of extra space

#### Example
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

## Running the Code
To run any solution:
```bash
python <filename>.py
```

For example:
```bash
python reverse_linked_list.py
python remove_nth_from_end.py
```

Each solution includes helper functions to create and print linked lists for testing purposes.

## Progress Tracker

### Completed Problems
- [x] Reverse Linked List (LeetCode #206)
- [x] Remove Nth Node From End of List (LeetCode #19)

### In Progress
- [ ] Merge Two Sorted Lists (LeetCode #21)
- [ ] Linked List Cycle (LeetCode #141)

### Next Up
- [ ] Add Two Numbers (LeetCode #2)
- [ ] Remove Duplicates from Sorted List (LeetCode #83)

---
*Note: This repository is part of my daily coding practice and DSA learning journey. Last updated: 2024-03-19* 
=======
# Binary Search Tree Implementation and Common Problems

This repository contains a Python implementation of a Binary Search Tree (BST) along with solutions to common BST-related interview questions.

## Problems Implemented

1. **Basic BST Operations**
   - Insertion of nodes
   - Searching for a value
   - Inorder traversal

2. **Common Interview Questions**
   - Finding minimum value in BST
   - Finding maximum value in BST
   - Validating if a tree is a valid BST

## Time Complexities

- **Insertion**: O(h) where h is the height of the tree
- **Search**: O(h)
- **Traversal**: O(n) where n is the number of nodes
- **Find Min/Max**: O(h)
- **Validate BST**: O(n)

In a balanced BST, h = log(n), making operations efficient. However, in worst case (skewed tree), h = n.

## Usage

```python
# Create a BST
bst = BinarySearchTree()

# Insert values
bst.insert(50)
bst.insert(30)
bst.insert(70)

# Search for a value
result = bst.search(30)  # Returns True

# Get inorder traversal
traversal = bst.inorder_traversal(bst.root)  # Returns [20, 30, 40, 50, 60, 70, 80]

# Find min and max
min_val = bst.find_min()  # Returns minimum value
max_val = bst.find_max()  # Returns maximum value

# Check if tree is valid BST
is_valid = bst.is_valid_bst()  # Returns True/False
``` 
>>>>>>> 51d1012 (Added BST implementation with common interview problems)
