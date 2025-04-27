def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without repeating characters
    """
    if not s:
        return 0
        
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If the current character is in the set, move the left pointer
        # and remove characters until the current character is not in the set
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            
        # Add the current character to the set
        char_set.add(s[right])
        
        # Update the maximum length
        max_length = max(max_length, right - left + 1)
        
    return max_length

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "abcabcbb"
    print(f"Input: '{s1}'")
    print(f"Output: {length_of_longest_substring(s1)}")  # Expected: 3
    
    # Test case 2
    s2 = "bbbbb"
    print(f"\nInput: '{s2}'")
    print(f"Output: {length_of_longest_substring(s2)}")  # Expected: 1
    
    # Test case 3
    s3 = "pwwkew"
    print(f"\nInput: '{s3}'")
    print(f"Output: {length_of_longest_substring(s3)}")  # Expected: 3 