"""
704. Binary Search
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, 
return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Perform binary search on a sorted array.
        
        Time Complexity: O(log n) - we halve the search space each iteration
        Space Complexity: O(1) - we only use constant extra space
        
        Args:
            nums: A sorted list of integers
            target: The integer to search for
            
        Returns:
            The index of target if found, otherwise -1
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2  # Prevents potential overflow
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    def search_recursive(self, nums: List[int], target: int) -> int:
        """
        Perform binary search recursively.
        
        Time Complexity: O(log n) - we halve the search space each call
        Space Complexity: O(log n) - due to recursion stack
        
        Args:
            nums: A sorted list of integers
            target: The integer to search for
            
        Returns:
            The index of target if found, otherwise -1
        """
        def binary_search(left, right):
            if left > right:
                return -1
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid - 1)
        
        return binary_search(0, len(nums) - 1)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Target exists in the middle
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    assert solution.search(nums1, target1) == 4
    assert solution.search_recursive(nums1, target1) == 4
    
    # Test case 2: Target does not exist
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    assert solution.search(nums2, target2) == -1
    assert solution.search_recursive(nums2, target2) == -1
    
    # Test case 3: Target is the first element
    nums3 = [-1, 0, 3, 5, 9, 12]
    target3 = -1
    assert solution.search(nums3, target3) == 0
    assert solution.search_recursive(nums3, target3) == 0
    
    # Test case 4: Target is the last element
    nums4 = [-1, 0, 3, 5, 9, 12]
    target4 = 12
    assert solution.search(nums4, target4) == 5
    assert solution.search_recursive(nums4, target4) == 5
    
    # Test case 5: Single element array (target exists)
    nums5 = [5]
    target5 = 5
    assert solution.search(nums5, target5) == 0
    assert solution.search_recursive(nums5, target5) == 0
    
    # Test case 6: Single element array (target does not exist)
    nums6 = [5]
    target6 = 3
    assert solution.search(nums6, target6) == -1
    assert solution.search_recursive(nums6, target6) == -1
    
    # Test case 7: Two elements
    nums7 = [1, 3]
    target7 = 3
    assert solution.search(nums7, target7) == 1
    assert solution.search_recursive(nums7, target7) == 1
    
    print("All tests passed!")