from typing import List

class Solution:
    def missing_number_sum(self, nums: List[int]) -> int:
        """
        Using sum of arithmetic series.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    def missing_number_xor(self, nums: List[int]) -> int:
        """
        Using XOR operation.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    def missing_number_sort(self, nums: List[int]) -> int:
        """
        Using sorting and linear scan.
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

    def missing_number_hash(self, nums: List[int]) -> int:
        """
        Using hash set.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i
        return -1

def test_solution():
    solution = Solution()
    
    # Test Case 1: Missing middle number
    nums = [0, 1, 3]
    print("Test Case 1:")
    print(f"Input: {nums}")
    print(f"Sum Method: {solution.missing_number_sum(nums)}")
    print(f"XOR Method: {solution.missing_number_xor(nums)}")
    print(f"Sort Method: {solution.missing_number_sort(nums)}")
    print(f"Hash Method: {solution.missing_number_hash(nums)}")
    print()
    
    # Test Case 2: Missing last number
    nums = [0, 1, 2]
    print("Test Case 2:")
    print(f"Input: {nums}")
    print(f"Sum Method: {solution.missing_number_sum(nums)}")
    print(f"XOR Method: {solution.missing_number_xor(nums)}")
    print(f"Sort Method: {solution.missing_number_sort(nums)}")
    print(f"Hash Method: {solution.missing_number_hash(nums)}")
    print()
    
    # Test Case 3: Missing first number
    nums = [1, 2, 3]
    print("Test Case 3:")
    print(f"Input: {nums}")
    print(f"Sum Method: {solution.missing_number_sum(nums)}")
    print(f"XOR Method: {solution.missing_number_xor(nums)}")
    print(f"Sort Method: {solution.missing_number_sort(nums)}")
    print(f"Hash Method: {solution.missing_number_hash(nums)}")
    print()
    
    # Test Case 4: Single element
    nums = [0]
    print("Test Case 4:")
    print(f"Input: {nums}")
    print(f"Sum Method: {solution.missing_number_sum(nums)}")
    print(f"XOR Method: {solution.missing_number_xor(nums)}")
    print(f"Sort Method: {solution.missing_number_sort(nums)}")
    print(f"Hash Method: {solution.missing_number_hash(nums)}")
    print()
    
    # Test Case 5: Large array
    nums = [i for i in range(100) if i != 42]
    print("Test Case 5:")
    print(f"Input: [0,1,...,41,43,...,99]")
    print(f"Sum Method: {solution.missing_number_sum(nums)}")
    print(f"XOR Method: {solution.missing_number_xor(nums)}")
    print(f"Sort Method: {solution.missing_number_sort(nums)}")
    print(f"Hash Method: {solution.missing_number_hash(nums)}")

if __name__ == "__main__":
    test_solution() 