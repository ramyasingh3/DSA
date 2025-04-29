"""
Valid Parentheses Implementation

This file contains an implementation of the Valid Parentheses problem using a stack approach.

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_valid_parentheses(s):
    """
    Check if the given string has valid parentheses using a stack.
    
    Args:
        s (str): String containing parentheses
        
    Returns:
        bool: True if parentheses are valid, False otherwise
    """
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # Stack to keep track of opening brackets
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.append(char)
        # If it's a closing bracket
        elif char in ')}]':
            # If stack is empty or top of stack doesn't match
            if not stack or stack.pop() != bracket_map[char]:
                return False
    
    # Stack should be empty if all brackets are properly matched
    return len(stack) == 0

def test_valid_parentheses():
    """Test cases for valid parentheses implementation"""
    # Test case 1: Simple valid case
    assert is_valid_parentheses("()") == True, "Test case 1 failed"
    
    # Test case 2: Multiple valid pairs
    assert is_valid_parentheses("()[]{}") == True, "Test case 2 failed"
    
    # Test case 3: Nested valid pairs
    assert is_valid_parentheses("([{}])") == True, "Test case 3 failed"
    
    # Test case 4: Invalid case - mismatched brackets
    assert is_valid_parentheses("(]") == False, "Test case 4 failed"
    
    # Test case 5: Invalid case - unclosed bracket
    assert is_valid_parentheses("(") == False, "Test case 5 failed"
    
    # Test case 6: Invalid case - extra closing bracket
    assert is_valid_parentheses(")") == False, "Test case 6 failed"
    
    # Test case 7: Complex valid case
    assert is_valid_parentheses("{[()()]}") == True, "Test case 7 failed"
    
    # Test case 8: Complex invalid case
    assert is_valid_parentheses("{[()(]}") == False, "Test case 8 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_valid_parentheses()
    
    # Example usage
    test_strings = [
        "()",
        "()[]{}",
        "([{}])",
        "(]",
        "(",
        ")",
        "{[()()]}",
        "{[()(]}"
    ]
    
    print("\nTesting various strings:")
    for s in test_strings:
        result = is_valid_parentheses(s)
        print(f"String: {s:<10} Valid: {result}") 