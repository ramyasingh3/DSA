def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Find the length of the longest common subsequence between two strings.
    
    Args:
        text1: First input string
        text2: Second input string
        
    Returns:
        Length of the longest common subsequence
    """
    m, n = len(text1), len(text2)
    # Create a DP table of size (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[m][n]

# Example usage
if __name__ == "__main__":
    # Test case 1
    text1 = "abcde"
    text2 = "ace"
    print(f"Input: text1 = {text1}, text2 = {text2}")
    print(f"Output: {longest_common_subsequence(text1, text2)}")  # Expected: 3 (ace)
    
    # Test case 2
    text3 = "abc"
    text4 = "def"
    print(f"\nInput: text1 = {text3}, text2 = {text4}")
    print(f"Output: {longest_common_subsequence(text3, text4)}")  # Expected: 0 