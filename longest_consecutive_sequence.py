from typing import List

def longest_consecutive_sequence(nums: List[int]) -> int:
    """
    Find the length of the longest consecutive sequence in an unsorted array.
    
    Args:
        nums: List of integers (can be unsorted)
        
    Returns:
        Length of the longest consecutive sequence
        
    Example:
        Input: [100, 4, 200, 1, 3, 2]
        Output: 4 (The longest consecutive sequence is [1, 2, 3, 4])
    """
    if not nums:
        return 0
        
    num_set = set(nums)
    max_length = 0
    
    for num in nums:
        # Only start checking sequences from the smallest number in the sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Keep checking for consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
                
            max_length = max(max_length, current_length)
            
    return max_length

def test_longest_consecutive_sequence():
    # Test case 1: Regular case
    assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4
    
    # Test case 2: Empty array
    assert longest_consecutive_sequence([]) == 0
    
    # Test case 3: Single element
    assert longest_consecutive_sequence([1]) == 1
    
    # Test case 4: No consecutive sequence
    assert longest_consecutive_sequence([2, 4, 6, 8]) == 1
    
    # Test case 5: Multiple sequences
    assert longest_consecutive_sequence([1, 2, 3, 10, 11, 12, 13]) == 4
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_consecutive_sequence()
