# Valid Parentheses

## Problem Description
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Example 1:
```
Input: s = "()"
Output: true
```

### Example 2:
```
Input: s = "()[]{}"
Output: true
```

### Example 3:
```
Input: s = "(]"
Output: false
```

### Example 4:
```
Input: s = "([)]"
Output: false
```

### Example 5:
```
Input: s = "{[]}"
Output: true
```

## Approach
The solution uses a stack data structure:

1. Create a map of closing to opening parentheses
2. Initialize an empty stack
3. Iterate through each character in the string:
   - If the character is a closing parenthesis:
     - Check if the stack is empty or if the top element doesn't match
     - If either condition is true, return false
     - Otherwise, pop the top element from the stack
   - If the character is an opening parenthesis, push it onto the stack
4. After processing all characters, return true if the stack is empty, false otherwise

## Time Complexity
- O(n), where n is the length of the string
- We process each character in the string exactly once

## Space Complexity
- O(n)
- In the worst case, we push all opening parentheses onto the stack
- The stack can grow up to the size of the input string

## Solution Code
The solution is implemented in `valid_parentheses.py` with detailed comments and example usage. 