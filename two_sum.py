from typing import List, Dict

class Solution:
    def two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force solution with O(n^2) time complexity.
        Checks every possible pair of numbers.
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def two_sum_hash_map(self, nums: List[int], target: int) -> List[int]:
        """
        Hash map solution with O(n) time complexity.
        Uses a dictionary to store complements.
        """
        seen: Dict[int, int] = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

    def two_sum_sorted(self, nums: List[int], target: int) -> List[int]:
        """
        Two-pointer solution with O(n log n) time complexity.
        Only returns the indices if the input array is already sorted.
        """
        # Create array of (value, index) pairs to preserve original indices
        pairs = [(num, i) for i, num in enumerate(nums)]
        pairs.sort()  # Sort by value
        
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = pairs[left][0] + pairs[right][0]
            if current_sum == target:
                return [pairs[left][1], pairs[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Test Case 1:")
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums1, target1)}")
    print(f"Hash Map: {solution.two_sum_hash_map(nums1, target1)}")
    print(f"Sorted: {solution.two_sum_sorted(nums1, target1)}")
    print()
    
    # Test Case 2: Multiple valid pairs
    nums2 = [3, 2, 4]
    target2 = 6
    print("Test Case 2:")
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums2, target2)}")
    print(f"Hash Map: {solution.two_sum_hash_map(nums2, target2)}")
    print(f"Sorted: {solution.two_sum_sorted(nums2, target2)}")
    print()
    
    # Test Case 3: Same number used twice
    nums3 = [3, 3]
    target3 = 6
    print("Test Case 3:")
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums3, target3)}")
    print(f"Hash Map: {solution.two_sum_hash_map(nums3, target3)}")
    print(f"Sorted: {solution.two_sum_sorted(nums3, target3)}")
    print()
    
    # Test Case 4: No solution
    nums4 = [1, 2, 3, 4]
    target4 = 10
    print("Test Case 4:")
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums4, target4)}")
    print(f"Hash Map: {solution.two_sum_hash_map(nums4, target4)}")
    print(f"Sorted: {solution.two_sum_sorted(nums4, target4)}")
    print()
    
    # Test Case 5: Negative numbers
    nums5 = [-1, -2, -3, -4, -5]
    target5 = -8
    print("Test Case 5:")
    print(f"Input: nums = {nums5}, target = {target5}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums5, target5)}")
    print(f"Hash Map: {solution.two_sum_hash_map(nums5, target5)}")
    print(f"Sorted: {solution.two_sum_sorted(nums5, target5)}")

if __name__ == "__main__":
    test_solution() 