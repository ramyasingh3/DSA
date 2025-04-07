# Palindrome Number

## Problem Description
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise. A palindrome number reads the same backward as forward.

## Examples
1. Positive palindrome:
   ```
   Input: 121
   Output: True
   ```

2. Negative number:
   ```
   Input: -121
   Output: False
   ```

3. Non-palindrome:
   ```
   Input: 123
   Output: False
   ```

4. Single digit:
   ```
   Input: 5
   Output: True
   ```

5. Number ending with zero:
   ```
   Input: 10
   Output: False
   ```

## Solution Approaches

### 1. String-based Solution (O(n))
- Convert the number to a string
- Compare the string with its reverse
- Return true if they match

### 2. Number-based Solution (O(log n))
- Handle edge cases (negative numbers, numbers ending with zero)
- Reverse half of the number
- Compare the original half with the reversed half
- Return true if they match

## Time Complexity
- String Solution: O(n)
- Number Solution: O(log n)

## Space Complexity
- String Solution: O(n)
- Number Solution: O(1)

## Usage
```python
from palindrome_number import Solution

solution = Solution()
x = 121

# Using string solution
result = solution.is_palindrome_string(x)
print(result)  # Output: True

# Using number solution (recommended)
result = solution.is_palindrome_number(x)
print(result)  # Output: True
```

## Common Applications
- Number validation
- Data integrity checks
- Cryptography
- Game development
- Mathematical computations 