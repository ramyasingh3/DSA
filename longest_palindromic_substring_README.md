# Longest Palindromic Substring

## Problem Description
Given a string `s`, return the longest palindromic substring in `s`. A palindrome is a string that reads the same backward as forward.

### Examples
1. Input: s = "babad"
   Output: "bab" or "aba"
   Explanation: Both "bab" and "aba" are valid answers.

2. Input: s = "cbbd"
   Output: "bb"
   Explanation: The longest palindromic substring is "bb".

3. Input: s = "a"
   Output: "a"
   Explanation: The single character is a palindrome.

## Approach
The solution uses an expansion around center technique:
1. For each character in the string, consider it as the center of a palindrome.
2. Expand around the center to find the longest palindrome.
3. Handle both odd-length (single center) and even-length (two centers) palindromes.
4. Keep track of the longest palindrome found during the expansion.

## Time Complexity
- O(n²) where n is the length of the string
- For each character, we expand around the center which takes O(n) time
- There are 2n-1 possible centers (n for odd-length, n-1 for even-length)

## Space Complexity
- O(1) for the pointers and variables
- No additional space is used for storing the result
- Overall: O(1) 