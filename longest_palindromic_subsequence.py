def longest_palindromic_subsequence(s: str) -> int:
    """
    Find the length of the longest palindromic subsequence in a string.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest palindromic subsequence
    """
    n = len(s)
    # Create a DP table of size n x n
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
        
    # Check for subsequences of length 2 and more
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # If first and last characters are same
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # If first and last characters are different
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                
    return dp[0][n - 1]

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "bbbab"
    print(f"Input: {s1}")
    print(f"Output: {longest_palindromic_subsequence(s1)}")  # Expected: 4 (bbbb)
    
    # Test case 2
    s2 = "cbbd"
    print(f"\nInput: {s2}")
    print(f"Output: {longest_palindromic_subsequence(s2)}")  # Expected: 2 (bb) 