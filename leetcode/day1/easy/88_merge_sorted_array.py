"""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two 
integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside 
the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements 
denote the elements that should be merged, and the last n elements are set to 0 and should be 
ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [0] and [1].
The result of the merge is [1].

Constraints:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 0 <= m, n <= 200
- -10^9 <= nums1[i], nums2[i] <= 10^9
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 as one sorted array.
        
        Time Complexity: O(m + n) - we process each element exactly once
        Space Complexity: O(1) - we modify nums1 in-place
        
        Args:
            nums1: First sorted array with enough space to hold both arrays
            m: Number of valid elements in nums1
            nums2: Second sorted array
            n: Number of elements in nums2
            
        Returns:
            None (modifies nums1 in-place)
        """
        # Start from the end of both arrays
        # p1 points to the last valid element in nums1
        # p2 points to the last element in nums2
        # p points to the last position in nums1 (where we'll place elements)
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them
        # (No need to copy from nums1 as they're already in place)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Normal case
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]
    
    # Test case 2: nums2 is empty
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1]
    
    # Test case 3: nums1 is empty initially
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1]
    
    # Test case 4: All elements in nums2 are smaller
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 3, 4, 5, 6]
    
    # Test case 5: All elements in nums1 are smaller
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [4, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 3, 4, 5, 6]
    
    # Test case 6: Duplicate values
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]
    
    print("All tests passed!")