"""
55. Jump Game
https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 2 no matter what. 
Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determine if you can reach the last index using greedy approach.
        
        Time Complexity: O(n) - we make one pass through the array
        Space Complexity: O(1) - we only use a few variables
        
        Args:
            nums: List of integers representing maximum jump lengths
            
        Returns:
            True if you can reach the last index, False otherwise
        """
        max_reach = 0  # The farthest index we can reach
        
        for i, jump in enumerate(nums):
            # If current position is beyond our maximum reach, we can't proceed
            if i > max_reach:
                return False
            
            # Update maximum reach
            max_reach = max(max_reach, i + jump)
            
            # If we can already reach or exceed the last index, return True
            if max_reach >= len(nums) - 1:
                return True
        
        return max_reach >= len(nums) - 1
    
    def canJump_dp(self, nums: List[int]) -> bool:
        """
        Determine if you can reach the last index using dynamic programming.
        
        Time Complexity: O(n^2) - nested loops in worst case
        Space Complexity: O(n) - we store the dp array
        
        Args:
            nums: List of integers representing maximum jump lengths
            
        Returns:
            True if you can reach the last index, False otherwise
        """
        if not nums:
            return False
        
        n = len(nums)
        # dp[i] is True if we can reach index i
        dp = [False] * n
        dp[0] = True  # We start at index 0
        
        for i in range(n):
            if dp[i]:  # If we can reach index i
                # Try all possible jumps from index i
                for j in range(1, nums[i] + 1):
                    if i + j < n:
                        dp[i + j] = True
                    else:
                        # We can reach or exceed the last index
                        return True
        
        return dp[-1]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Can reach the end
    nums1 = [2, 3, 1, 1, 4]
    assert solution.canJump(nums1) == True
    assert solution.canJump_dp(nums1) == True
    
    # Test case 2: Cannot reach the end
    nums2 = [3, 2, 1, 0, 4]
    assert solution.canJump(nums2) == False
    assert solution.canJump_dp(nums2) == False
    
    # Test case 3: Single element (already at end)
    nums3 = [0]
    assert solution.canJump(nums3) == True
    assert solution.canJump_dp(nums3) == True
    
    # Test case 4: Can jump directly to end
    nums4 = [4, 0, 0, 0, 0]
    assert solution.canJump(nums4) == True
    assert solution.canJump_dp(nums4) == True
    
    # Test case 5: Need multiple jumps
    nums5 = [1, 1, 1, 1, 1]
    assert solution.canJump(nums5) == True
    assert solution.canJump_dp(nums5) == True
    
    # Test case 6: Blocked by zero
    nums6 = [3, 2, 1, 0, 0, 0]
    assert solution.canJump(nums6) == False
    assert solution.canJump_dp(nums6) == False
    
    # Test case 7: Large jump at beginning
    nums7 = [5, 0, 0, 0, 0, 0]
    assert solution.canJump(nums7) == True
    assert solution.canJump_dp(nums7) == True
    
    print("All tests passed!")