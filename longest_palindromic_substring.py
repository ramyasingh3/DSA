class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring in s.
        
        Args:
            s: The input string
            
        Returns:
            str: The longest palindromic substring
        """
        if not s:
            return ""
            
        start = 0
        end = 0
        
        for i in range(len(s)):
            # Check for odd-length palindrome
            len1 = self.expandAroundCenter(s, i, i)
            # Check for even-length palindrome
            len2 = self.expandAroundCenter(s, i, i + 1)
            # Get the maximum length
            max_len = max(len1, len2)
            
            # Update start and end if we found a longer palindrome
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]
        
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        """
        Helper function to expand around the center and find the length of the palindrome.
        
        Args:
            s: The input string
            left: Left index to start expansion
            right: Right index to start expansion
            
        Returns:
            int: Length of the palindrome
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

def test_longest_palindrome():
    # Test cases
    test_cases = [
        ("babad", ["bab", "aba"]),  # Multiple valid answers
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("", [""]),
        ("racecar", ["racecar"]),
        ("abacdfgdcaba", ["aba"]),
        ("aaabaaaa", ["aaabaaa"]),
    ]
    
    solver = LongestPalindromicSubstring()
    
    for s, expected_list in test_cases:
        result = solver.longestPalindrome(s)
        print(f"Input: s = '{s}'")
        print(f"Output: '{result}'")
        print(f"Expected one of: {expected_list}")
        print(f"Test {'passed' if result in expected_list else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_longest_palindrome() 