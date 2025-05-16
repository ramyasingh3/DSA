import bisect

def length_of_lis(nums: list[int]) -> int:
    """
    Find the length of the longest strictly increasing subsequence.
    
    Args:
        nums: List of integers
        
    Returns:
        Length of the longest increasing subsequence
    """
    if not nums:
        return 0
        
    # dp[i] represents the length of LIS ending at index i
    dp = [1] * len(nums)
    
    # For each position, check all previous positions
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Input: nums = {nums1}")
    print(f"Output: {length_of_lis(nums1)}")  # Expected: 4 (2, 5, 7, 101)
    
    # Test case 2
    nums2 = [0, 1, 0, 3, 2, 3]
    print(f"\nInput: nums = {nums2}")
    print(f"Output: {length_of_lis(nums2)}")  # Expected: 4 (0, 1, 2, 3)
    
    # Test case 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    print(f"\nInput: nums = {nums3}")
    print(f"Output: {length_of_lis(nums3)}")  # Expected: 1 (7)

    # Additional test cases
    nums4 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    assert length_of_lis(nums4) == 6
    
    nums5 = []
    assert length_of_lis(nums5) == 0
    
    print("All test cases passed!") 