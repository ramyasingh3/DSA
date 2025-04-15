class MinimumWindowSubstring:
    def minWindow(self, s: str, t: str) -> str:
        """
        Find the minimum window in s which will contain all the characters in t.
        
        Args:
            s: The source string
            t: The target string containing characters to find
            
        Returns:
            str: The minimum window substring, or empty string if not found
        """
        if not s or not t or len(s) < len(t):
            return ""
            
        # Initialize character count maps
        target_counts = {}
        window_counts = {}
        
        # Count characters in t
        for char in t:
            target_counts[char] = target_counts.get(char, 0) + 1
            
        required = len(target_counts)  # Number of unique characters needed
        formed = 0  # Number of unique characters formed in current window
        
        # Initialize sliding window variables
        left = 0
        min_len = float('inf')
        result = ""
        
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if current character completes a required character
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
                
            # Try to contract the window from the left
            while left <= right and formed == required:
                # Update result if current window is smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]
                    
                # Move left pointer
                left_char = s[left]
                window_counts[left_char] -= 1
                
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed -= 1
                    
                left += 1
                
        return result

def test_min_window():
    # Test cases
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("aa", "aa", "aa"),
        ("abc", "ac", "abc"),
        ("", "a", ""),
        ("a", "", ""),
    ]
    
    solver = MinimumWindowSubstring()
    
    for s, t, expected in test_cases:
        result = solver.minWindow(s, t)
        print(f"Input: s = '{s}', t = '{t}'")
        print(f"Output: '{result}'")
        print(f"Expected: '{expected}'")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_min_window() 