"""
Find the length of the longest consecutive elements sequence in an unsorted array.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive elements sequence is [0,1,2,3,4,5,6,7,8].

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

def longest_consecutive(nums: List[int]) -> int:
    """
    Solution using a hash set for O(1) lookups.
    The key insight is that we only need to start counting from the smallest number
    in each potential sequence (i.e., numbers that don't have a predecessor).
    """
    if not nums:
        return 0
    
    # Convert to set for O(1) lookups
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start counting from the smallest number in a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

# Test cases
def test_longest_consecutive():
    test_cases = [
        ([100,4,200,1,3,2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
        ([], 0),
        ([1], 1),
        ([1,3,5,7], 1),
        ([1,2,3,4,5], 5),
        ([1,1,1,1], 1),
        ([1,2,0,1], 3),
    ]
    
    for nums, expected in test_cases:
        result = longest_consecutive(nums)
        assert result == expected, f"Failed for {nums}. Expected {expected}, got {result}"
        print(f"Test passed for nums={nums}")

if __name__ == "__main__":
    test_longest_consecutive()
