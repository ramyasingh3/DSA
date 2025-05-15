def climb_stairs(n: int) -> int:
    """
    Find the number of distinct ways to climb to the top of n stairs.
    Each time you can either climb 1 or 2 steps.
    
    Args:
        n: Number of stairs to climb
        
    Returns:
        Number of distinct ways to climb to the top
    """
    if n <= 2:
        return n
        
    # Space optimized solution using only two variables
    prev2, prev1 = 1, 2  # Base cases for n=1 and n=2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1

# Example usage
if __name__ == "__main__":
    # Test case 1
    n1 = 3
    print(f"Input: n = {n1}")
    print(f"Output: {climb_stairs(n1)}")  # Expected: 3 (1+1+1, 1+2, 2+1)
    
    # Test case 2
    n2 = 4
    print(f"\nInput: n = {n2}")
    print(f"Output: {climb_stairs(n2)}")  # Expected: 5 (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)
    
    # Test case 3
    n3 = 5
    print(f"\nInput: n = {n3}")
    print(f"Output: {climb_stairs(n3)}")  # Expected: 8 