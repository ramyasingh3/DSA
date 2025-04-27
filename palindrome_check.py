"""
Problem: Valid Palindrome

Write a function that checks if a given string is a palindrome.
A string is a palindrome if it reads the same forwards and backwards.
The function should:
1. Convert all characters to lowercase
2. Remove all non-alphanumeric characters
3. Return True if the string is a palindrome, False otherwise

Example:
Input: "A man, a plan, a canal: Panama"
Output: True  # Because "amanaplanacanalpanama" is a palindrome

Input: "race a car"
Output: False  # Because "raceacar" is not a palindrome
"""

def is_palindrome(s: str) -> bool:
    # Convert to lowercase and keep only alphanumeric characters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare string with its reverse
    return cleaned == cleaned[::-1]

def test_palindrome():
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("hello", False),
        ("", True),  # Empty string is considered palindrome
        ("12321", True),
        ("12345", False),
        ("!@#$%", True),  # String with only special chars becomes empty string
    ]
    
    for test_str, expected in test_cases:
        result = is_palindrome(test_str)
        print(f"String: '{test_str}'")
        print(f"Expected: {expected}, Got: {result}")
        print("Test Passed" if result == expected else "Test Failed")
        print("-" * 50)

if __name__ == "__main__":
    test_palindrome()
