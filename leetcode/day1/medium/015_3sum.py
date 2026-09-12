"""
15. 3Sum
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = (-1) + 2 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,-1,2] and [-1,0,1].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
- 0 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the array that sum up to zero.
        
        Time Complexity: O(n^2) - we sort the array (O(n log n)) then use two pointers for each element
        Space Complexity: O(1) or O(n) depending on sorting algorithm (we ignore output space)
        
        Args:
            nums: List of integers
            
        Returns:
            List of unique triplets that sum to zero
        """
        nums.sort()  # Sort the array to use two-pointer technique
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Since array is sorted, if the current number is positive, 
            # we can't get a sum of zero with larger numbers
            if nums[i] > 0:
                break
            
            # Use two pointers to find pairs that sum to -nums[i]
            left, right = i + 1, n - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < target:
                    # Need a larger sum, move left pointer right
                    left += 1
                else:
                    # Need a smaller sum, move right pointer left
                    right -= 1
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Normal case with multiple solutions
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    # Sort both for comparison since order doesn't matter
    assert sorted([sorted(triplet) for triplet in result1]) == sorted([sorted(triplet) for triplet in expected1])
    
    # Test case 2: No solution
    nums2 = [0, 1, 1]
    result2 = solution.threeSum(nums2)
    assert result2 == []
    
    # Test case 3: All zeros
    nums3 = [0, 0, 0]
    result3 = solution.threeSum(nums3)
    assert result3 == [[0, 0, 0]]
    
    # Test case 4: Empty array
    nums4 = []
    result4 = solution.threeSum(nums4)
    assert result4 == []
    
    # Test case 5: Single element
    nums5 = [1]
    result5 = solution.threeSum(nums5)
    assert result5 == []
    
    # Test case 6: Two elements
    nums6 = [1, 2]
    result6 = solution.threeSum(nums6)
    assert result6 == []
    
    # Test case 7: All negative numbers
    nums7 = [-2, -1, 0, 1, 2]
    result7 = solution.threeSum(nums7)
    expected7 = [[-2, 0, 2], [-1, 0, 1]]
    assert sorted([sorted(triplet) for triplet in result7]) == sorted([sorted(triplet) for triplet in expected7])
    
    print("All tests passed!")