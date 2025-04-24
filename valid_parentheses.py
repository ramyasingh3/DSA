def isValid(s: str) -> bool:
    """
    Check if the input string has valid parentheses.
    
    Args:
        s (str): Input string containing parentheses
        
    Returns:
        bool: True if the parentheses are valid, False otherwise
    """
    # Map of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in bracket_map:
            # If stack is empty or top element doesn't match
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            # Push opening bracket onto stack
            stack.append(char)
    
    # If stack is empty, all brackets were matched
    return not stack

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "()"
    print(f"Input: {s1}")
    print(f"Output: {isValid(s1)}")  # Expected: True
    
    # Test case 2
    s2 = "()[]{}"
    print(f"\nInput: {s2}")
    print(f"Output: {isValid(s2)}")  # Expected: True
    
    # Test case 3
    s3 = "(]"
    print(f"\nInput: {s3}")
    print(f"Output: {isValid(s3)}")  # Expected: False
    
    # Test case 4
    s4 = "([)]"
    print(f"\nInput: {s4}")
    print(f"Output: {isValid(s4)}")  # Expected: False
    
    # Test case 5
    s5 = "{[]}"
    print(f"\nInput: {s5}")
    print(f"Output: {isValid(s5)}")  # Expected: True 