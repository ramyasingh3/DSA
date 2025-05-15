def coin_change(coins: list[int], amount: int) -> int:
    """
    Find the fewest number of coins needed to make up a given amount.
    Uses dynamic programming.
    
    Args:
        coins: List of coin denominations
        amount: Target amount
        
    Returns:
        Minimum number of coins needed to make up the amount, or -1 if not possible
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
if __name__ == "__main__":
    # Test case 1
    coins1 = [1, 2, 5]
    amount1 = 11
    print(f"Input: coins = {coins1}, amount = {amount1}")
    print(f"Output: {coin_change(coins1, amount1)}")  # Expected: 3 (11 = 5+5+1)
    
    # Test case 2
    coins2 = [2]
    amount2 = 3
    print(f"\nInput: coins = {coins2}, amount = {amount2}")
    print(f"Output: {coin_change(coins2, amount2)}")  # Expected: -1 