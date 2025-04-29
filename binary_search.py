"""
Binary Search Implementation

This file contains an implementation of the binary search algorithm with detailed explanations
and test cases. Binary search is an efficient algorithm for finding an element in a sorted array.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binary_search(arr, target):
    """
    Performs binary search on a sorted array to find the target value.
    
    Args:
        arr (list): A sorted list of numbers
        target: The value to search for
        
    Returns:
        int: Index of the target if found, -1 if not found
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If target is found at mid, return the index
        if arr[mid] == target:
            return mid
            
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
            
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target not found
    return -1

def test_binary_search():
    """Test cases for binary search implementation"""
    # Test case 1: Target exists in array
    arr1 = [1, 3, 5, 7, 9, 11, 13, 15]
    assert binary_search(arr1, 7) == 3, "Test case 1 failed"
    
    # Test case 2: Target doesn't exist in array
    assert binary_search(arr1, 6) == -1, "Test case 2 failed"
    
    # Test case 3: Target is first element
    assert binary_search(arr1, 1) == 0, "Test case 3 failed"
    
    # Test case 4: Target is last element
    assert binary_search(arr1, 15) == 7, "Test case 4 failed"
    
    # Test case 5: Empty array
    assert binary_search([], 5) == -1, "Test case 5 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_binary_search()
    
    # Example usage
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element {target} is present at index {result}")
    else:
        print(f"Element {target} is not present in the array") 