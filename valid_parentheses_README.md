# Valid Parentheses

## Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
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
1. Initialize an empty stack
2. For each character in the string:
   - If it's an opening bracket, push it onto the stack
   - If it's a closing bracket:
     - Check if the stack is empty (invalid)
     - Check if the top of the stack matches the current closing bracket
     - If it matches, pop from the stack; otherwise, return false
3. After processing all characters, check if the stack is empty
   - If empty, all brackets were properly matched
   - If not empty, there are unmatched opening brackets

## Time Complexity
- O(n), where n is the length of the string
- We process each character exactly once

## Space Complexity
- O(n) in the worst case
- The stack can grow up to the size of the input string if all characters are opening brackets 