"""
Two Sum Problem Implementation

This file contains multiple implementations of the Two Sum problem:
1. Brute Force Approach (O(n²))
2. Hash Map Approach (O(n))

Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Time Complexity:
- Brute Force: O(n²)
- Hash Map: O(n)

Space Complexity:
- Brute Force: O(1)
- Hash Map: O(n)
"""

def two_sum_brute_force(nums, target):
    """
    Brute force approach to find two numbers that sum up to target.
    
    Args:
        nums (list): List of integers
        target (int): Target sum
        
    Returns:
        tuple: Indices of the two numbers that sum up to target
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

def two_sum_hash_map(nums, target):
    """
    Hash map approach to find two numbers that sum up to target.
    
    Args:
        nums (list): List of integers
        target (int): Target sum
        
    Returns:
        tuple: Indices of the two numbers that sum up to target
    """
    num_map = {}  # val -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return (num_map[complement], i)
        num_map[num] = i
    return None

def test_two_sum():
    """Test cases for both two sum implementations"""
    # Test case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    assert two_sum_brute_force(nums1, target1) == (0, 1), "Brute force test case 1 failed"
    assert two_sum_hash_map(nums1, target1) == (0, 1), "Hash map test case 1 failed"
    
    # Test case 2: Numbers at the end
    nums2 = [3, 2, 4]
    target2 = 6
    assert two_sum_brute_force(nums2, target2) == (1, 2), "Brute force test case 2 failed"
    assert two_sum_hash_map(nums2, target2) == (1, 2), "Hash map test case 2 failed"
    
    # Test case 3: Same number twice
    nums3 = [3, 3]
    target3 = 6
    assert two_sum_brute_force(nums3, target3) == (0, 1), "Brute force test case 3 failed"
    assert two_sum_hash_map(nums3, target3) == (0, 1), "Hash map test case 3 failed"
    
    # Test case 4: No solution
    nums4 = [1, 2, 3, 4]
    target4 = 10
    assert two_sum_brute_force(nums4, target4) is None, "Brute force test case 4 failed"
    assert two_sum_hash_map(nums4, target4) is None, "Hash map test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_two_sum()
    
    # Example usage
    nums = [2, 7, 11, 15]
    target = 9
    
    # Using brute force approach
    result_brute = two_sum_brute_force(nums, target)
    print(f"Brute Force Result: {result_brute}")
    
    # Using hash map approach
    result_hash = two_sum_hash_map(nums, target)
    print(f"Hash Map Result: {result_hash}")
    
    if result_hash:
        print(f"Numbers at indices {result_hash} sum up to {target}")
        print(f"Numbers are: {nums[result_hash[0]]} and {nums[result_hash[1]]}") 