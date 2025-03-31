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

---
*Note: This repository is part of my daily coding practice and DSA learning journey.* 