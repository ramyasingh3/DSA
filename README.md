# Reverse Linked List

This is a solution for LeetCode problem #206: Reverse Linked List.

## Problem Description
Given the head of a singly linked list, reverse the list, and return the reversed list.

## Solution Approach
The solution uses an iterative approach to reverse the linked list:
1. Initialize a `prev` pointer as `None` (this will be the new head of the reversed list)
2. Keep track of the current node
3. For each node:
   - Store the next node temporarily
   - Reverse the link by pointing current node to previous node
   - Move the previous and current pointers forward
4. Return the new head (which will be the last node of the original list)

## Time Complexity
- O(n) where n is the number of nodes in the linked list

## Space Complexity
- O(1) as we only use a constant amount of extra space

## Example
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1

## Running the Code
To run the solution:
```bash
python reverse_linked_list.py
```

The code includes helper functions to create and print linked lists for testing purposes. 