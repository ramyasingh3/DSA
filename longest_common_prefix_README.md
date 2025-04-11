# Longest Common Prefix

## Problem Description
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

## Examples
1. Common prefix exists:
   ```
   Input: strs = ["flower", "flow", "flight"]
   Output: "fl"
   Explanation: All strings start with "fl".
   ```

2. No common prefix:
   ```
   Input: strs = ["dog", "racecar", "car"]
   Output: ""
   Explanation: There is no common prefix among the input strings.
   ```

3. Single string:
   ```
   Input: strs = ["a"]
   Output: "a"
   Explanation: The only string is its own prefix.
   ```

## Solution Approaches

### 1. Vertical Scanning (O(S))
- Compares characters vertically (column by column)
- Time Complexity: O(S), where S is the sum of all characters
- Space Complexity: O(1)
- Most efficient for most cases
- Stops early when mismatch found

### 2. Horizontal Scanning (O(S))
- Compares strings horizontally (pair by pair)
- Time Complexity: O(S), where S is the sum of all characters
- Space Complexity: O(1)
- Simple to understand
- Good for learning the concept

### 3. Divide and Conquer (O(S))
- Divides the problem into smaller subproblems
- Time Complexity: O(S), where S is the sum of all characters
- Space Complexity: O(m log n), where m is the length of the longest string
- More complex but educational
- Good for understanding divide and conquer

## Time Complexity
- Vertical Scanning: O(S)
- Horizontal Scanning: O(S)
- Divide and Conquer: O(S)

## Space Complexity
- Vertical Scanning: O(1)
- Horizontal Scanning: O(1)
- Divide and Conquer: O(m log n)

## Usage
```python
from longest_common_prefix import Solution

solution = Solution()
strs = ["flower", "flow", "flight"]

# Using vertical scanning
result = solution.longest_common_prefix_vertical(strs)
print(f"Longest common prefix: {result}")

# Using horizontal scanning
result = solution.longest_common_prefix_horizontal(strs)
print(f"Longest common prefix: {result}")

# Using divide and conquer
result = solution.longest_common_prefix_divide(strs)
print(f"Longest common prefix: {result}")
```

## Common Applications
- String matching
- Text processing
- DNA sequence analysis
- File path resolution
- URL routing 