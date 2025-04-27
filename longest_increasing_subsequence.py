import bisect

def length_of_lis(nums):
    """
    Find the length of the longest strictly increasing subsequence.
    
    Args:
        nums (List[int]): Input array of integers
        
    Returns:
        int: Length of the longest increasing subsequence
    """
    if not nums:
        return 0
        
    tails = []
    
    for num in nums:
        # Find the first element in tails that is >= num
        idx = bisect.bisect_left(tails, num)
        
        if idx == len(tails):
            # If num is larger than all elements in tails, append it
            tails.append(num)
        else:
            # Otherwise, replace the first element >= num with num
            tails[idx] = num
    
    return len(tails)

# Test cases
def test_length_of_lis():
    # Example 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    assert length_of_lis(nums1) == 4
    
    # Example 2
    nums2 = [0, 1, 0, 3, 2, 3]
    assert length_of_lis(nums2) == 4
    
    # Example 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    assert length_of_lis(nums3) == 1
    
    # Additional test cases
    nums4 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    assert length_of_lis(nums4) == 6
    
    nums5 = []
    assert length_of_lis(nums5) == 0
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_length_of_lis() 