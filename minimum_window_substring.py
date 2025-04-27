def min_window(s: str, t: str) -> str:
    """
    Find the minimum window in s which will contain all the characters in t.
    
    Args:
        s: The string to search in
        t: The string containing characters to find
        
    Returns:
        The minimum window substring
    """
    if not s or not t or len(s) < len(t):
        return ""
        
    # Create frequency maps
    t_freq = {}
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1
        
    required = len(t_freq)
    formed = 0
    window_freq = {}
    
    # Sliding window variables
    left = 0
    right = 0
    min_len = float('inf')
    result = ""
    
    while right < len(s):
        # Add current character to window
        char = s[right]
        window_freq[char] = window_freq.get(char, 0) + 1
        
        # Check if current character completes a required character
        if char in t_freq and window_freq[char] == t_freq[char]:
            formed += 1
            
        # Try to contract the window from the left
        while left <= right and formed == required:
            # Update result if current window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right+1]
                
            # Remove leftmost character from window
            char = s[left]
            window_freq[char] -= 1
            if char in t_freq and window_freq[char] < t_freq[char]:
                formed -= 1
            left += 1
            
        right += 1
        
    return result

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    print(f"Input: s = '{s1}', t = '{t1}'")
    print(f"Output: '{min_window(s1, t1)}'")  # Expected: "BANC"
    
    # Test case 2
    s2 = "a"
    t2 = "a"
    print(f"\nInput: s = '{s2}', t = '{t2}'")
    print(f"Output: '{min_window(s2, t2)}'")  # Expected: "a" 