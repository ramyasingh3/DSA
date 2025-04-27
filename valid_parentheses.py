def is_valid(s: str) -> bool:
    """
    Check if the input string has valid parentheses.
    
    Args:
        s: Input string containing parentheses
        
    Returns:
        True if the parentheses are valid, False otherwise
    """
    # Map of closing to opening parentheses
    parentheses_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in parentheses_map:
            # If stack is empty or top element doesn't match
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
            
    return not stack

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "()"
    print(f"Input: '{s1}'")
    print(f"Output: {is_valid(s1)}")  # Expected: True
    
    # Test case 2
    s2 = "()[]{}"
    print(f"\nInput: '{s2}'")
    print(f"Output: {is_valid(s2)}")  # Expected: True
    
    # Test case 3
    s3 = "(]"
    print(f"\nInput: '{s3}'")
    print(f"Output: {is_valid(s3)}")  # Expected: False
    
    # Test case 4
    s4 = "([)]"
    print(f"\nInput: {s4}")
    print(f"Output: {is_valid(s4)}")  # Expected: False
    
    # Test case 5
    s5 = "{[]}"
    print(f"\nInput: {s5}")
    print(f"Output: {is_valid(s5)}")  # Expected: True 