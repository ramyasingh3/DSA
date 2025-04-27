# Longest Palindromic Substring

## Problem Description
Given a string `s`, return the longest palindromic substring in `s`. A palindrome is a string that reads the same backward as forward.

### Example 1:
```
Input: s = "babad"
Output: "bab" or "aba"
Explanation: Both "bab" and "aba" are valid answers.
```

### Example 2:
```
Input: s = "cbbd"
Output: "bb"
Explanation: The longest palindromic substring is "bb".
```

## Approach
The solution uses an expand around center technique:

1. For each character in the string, consider it as the center of a potential palindrome
2. Expand around the center to find the longest palindrome:
   - For odd-length palindromes, expand with the same center
   - For even-length palindromes, expand with two adjacent centers
3. Keep track of the longest palindrome found
4. Return the substring corresponding to the longest palindrome

## Time Complexity
- O(n²), where n is the length of the string
- For each character in the string, we expand around the center which can take O(n) time
- In the worst case, we do this for each character

## Space Complexity
- O(1)
- We use constant extra space for variables to track the start and end of the longest palindrome

## Solution Code
The solution is implemented in `longest_palindromic_substring.py` with detailed comments and example usage. 