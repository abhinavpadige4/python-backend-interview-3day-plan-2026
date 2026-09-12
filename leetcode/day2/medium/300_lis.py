"""
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.

Example 3:
Input: nums = [7,7,7,7,7,7,7,7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.

Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4
"""

from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Find the length of the longest increasing subsequence using binary search.
        
        Time Complexity: O(n log n) - we iterate through nums and use binary search
        Space Complexity: O(n) - we store the tails array
        
        Args:
            nums: List of integers
            
        Returns:
            Length of the longest increasing subsequence
        """
        if not nums:
            return 0
        
        # tails[i] stores the smallest tail value of all increasing subsequences 
        # of length i+1
        tails = []
        
        for num in nums:
            # Find the position where num should be inserted in tails
            # Using bisect_left to maintain strictly increasing property
            pos = bisect.bisect_left(tails, num)
            
            if pos == len(tails):
                # num is greater than all elements in tails
                tails.append(num)
            else:
                # Replace the element at pos with num
                tails[pos] = num
        
        return len(tails)
    
    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        """
        Find the length of the longest increasing subsequence using dynamic programming.
        
        Time Complexity: O(n^2) - nested loops
        Space Complexity: O(n) - we store the dp array
        
        Args:
            nums: List of integers
            
        Returns:
            Length of the longest increasing subsequence
        """
        if not nums:
            return 0
        
        n = len(nums)
        # dp[i] represents the length of LIS ending at index i
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Normal case
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    assert solution.lengthOfLIS(nums1) == 4
    assert solution.lengthOfLIS_dp(nums1) == 4
    
    # Test case 2: Another normal case
    nums2 = [0, 1, 0, 3, 2, 3]
    assert solution.lengthOfLIS(nums2) == 4
    assert solution.lengthOfLIS_dp(nums2) == 4
    
    # Test case 3: All same elements
    nums3 = [7, 7, 7, 7, 7, 7, 7, 7]
    assert solution.lengthOfLIS(nums3) == 1
    assert solution.lengthOfLIS_dp(nums3) == 1
    
    # Test case 4: Strictly increasing
    nums4 = [1, 2, 3, 4, 5]
    assert solution.lengthOfLIS(nums4) == 5
    assert solution.lengthOfLIS_dp(nums4) == 5
    
    # Test case 5: Strictly decreasing
    nums5 = [5, 4, 3, 2, 1]
    assert solution.lengthOfLIS(nums5) == 1
    assert solution.lengthOfLIS_dp(nums5) == 1
    
    # Test case 6: Single element
    nums6 = [5]
    assert solution.lengthOfLIS(nums6) == 1
    assert solution.lengthOfLIS_dp(nums6) == 1
    
    # Test case 7: Empty array
    nums7 = []
    assert solution.lengthOfLIS(nums7) == 0
    assert solution.lengthOfLIS_dp(nums7) == 0
    
    print("All tests passed!")