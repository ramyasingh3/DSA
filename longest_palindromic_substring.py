def longest_palindrome(s: str) -> str:
    """
    Find the longest palindromic substring in s.
    
    Args:
        s: Input string
        
    Returns:
        The longest palindromic substring
    """
    if not s:
        return ""
        
    start = 0
    end = 0
    
    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
        
    for i in range(len(s)):
        # Check for odd length palindromes
        len1 = expand_around_center(i, i)
        # Check for even length palindromes
        len2 = expand_around_center(i, i + 1)
        
        # Get the maximum length
        max_len = max(len1, len2)
        
        # Update start and end if we found a longer palindrome
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            
    return s[start:end + 1]

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "babad"
    print(f"Input: '{s1}'")
    print(f"Output: '{longest_palindrome(s1)}'")  # Expected: "bab" or "aba"
    
    # Test case 2
    s2 = "cbbd"
    print(f"\nInput: '{s2}'")
    print(f"Output: '{longest_palindrome(s2)}'")  # Expected: "bb" 