# Minimum Window Substring

## Problem Description
Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return an empty string `""`.

### Examples
1. Input: s = "ADOBECODEBANC", t = "ABC"
   Output: "BANC"
   Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

2. Input: s = "a", t = "a"
   Output: "a"
   Explanation: The entire string s is the minimum window.

3. Input: s = "a", t = "aa"
   Output: ""
   Explanation: Both 'a's from t must be included in the window, but s only has one 'a'.

## Approach
The solution uses a sliding window technique with two pointers:
1. Use two pointers, `left` and `right`, to represent the window boundaries.
2. Move the `right` pointer to expand the window until it contains all characters from `t`.
3. Once all characters are found, move the `left` pointer to contract the window while maintaining the required characters.
4. Keep track of the minimum window size and its starting position.
5. Use a hash map to count the required characters and their frequencies.

## Time Complexity
- O(|S| + |T|) where |S| and |T| are the lengths of strings s and t
- Each character in s is visited at most twice (once by each pointer)

## Space Complexity
- O(|T|) for the hash map storing character counts
- O(1) for the pointers and counters
- Overall: O(|T|) 