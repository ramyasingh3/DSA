class Solution:
    def is_palindrome_string(self, x: int) -> bool:
        """
        String-based solution with O(n) time complexity.
        """
        return str(x) == str(x)[::-1]

    def is_palindrome_number(self, x: int) -> bool:
        """
        Number-based solution with O(log n) time complexity.
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_num = 0
        original = x
        
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
            
        return x == reversed_num or x == reversed_num // 10

def test_solution():
    solution = Solution()
    
    # Test Case 1: Positive palindrome
    x1 = 121
    print("Test Case 1:")
    print(f"Input: {x1}")
    print(f"String Solution: {solution.is_palindrome_string(x1)}")
    print(f"Number Solution: {solution.is_palindrome_number(x1)}")
    print()
    
    # Test Case 2: Negative number
    x2 = -121
    print("Test Case 2:")
    print(f"Input: {x2}")
    print(f"String Solution: {solution.is_palindrome_string(x2)}")
    print(f"Number Solution: {solution.is_palindrome_number(x2)}")
    print()
    
    # Test Case 3: Non-palindrome
    x3 = 123
    print("Test Case 3:")
    print(f"Input: {x3}")
    print(f"String Solution: {solution.is_palindrome_string(x3)}")
    print(f"Number Solution: {solution.is_palindrome_number(x3)}")
    print()
    
    # Test Case 4: Single digit
    x4 = 5
    print("Test Case 4:")
    print(f"Input: {x4}")
    print(f"String Solution: {solution.is_palindrome_string(x4)}")
    print(f"Number Solution: {solution.is_palindrome_number(x4)}")
    print()
    
    # Test Case 5: Number ending with zero
    x5 = 10
    print("Test Case 5:")
    print(f"Input: {x5}")
    print(f"String Solution: {solution.is_palindrome_string(x5)}")
    print(f"Number Solution: {solution.is_palindrome_number(x5)}")

if __name__ == "__main__":
    test_solution() 