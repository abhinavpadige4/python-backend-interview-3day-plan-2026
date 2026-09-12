"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
- n == height.length
- 0 <= n <= 3 * 10^4
- 0 <= height[i] <= 10^5
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculate trapped rain water using two-pointer approach.
        
        Time Complexity: O(n) - we make one pass through the array
        Space Complexity: O(1) - we only use a few variables
        
        Args:
            height: List of non-negative integers representing elevation map
            
        Returns:
            Total units of trapped rain water
        """
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water_trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1
        
        return water_trapped
    
    def trap_dp(self, height: List[int]) -> int:
        """
        Calculate trapped rain water using dynamic programming approach.
        
        Time Complexity: O(n) - we make three passes through the array
        Space Complexity: O(n) - we store left_max and right_max arrays
        
        Args:
            height: List of non-negative integers representing elevation map
            
        Returns:
            Total units of trapped rain water
        """
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        # Fill left_max array
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        
        # Fill right_max array
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        # Calculate trapped water
        water_trapped = 0
        for i in range(n):
            water_trapped += min(left_max[i], right_max[i]) - height[i]
        
        return water_trapped


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Normal case
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert solution.trap(height1) == 6
    assert solution.trap_dp(height1) == 6
    
    # Test case 2: Another normal case
    height2 = [4, 2, 0, 3, 2, 5]
    assert solution.trap(height2) == 9
    assert solution.trap_dp(height2) == 9
    
    # Test case 3: No water can be trapped
    height3 = [1, 2, 3, 4, 5]
    assert solution.trap(height3) == 0
    assert solution.trap_dp(height3) == 0
    
    # Test case 4: All same height
    height4 = [3, 3, 3, 3]
    assert solution.trap(height4) == 0
    assert solution.trap_dp(height4) == 0
    
    # Test case 5: Single element
    height5 = [5]
    assert solution.trap(height5) == 0
    assert solution.trap_dp(height5) == 0
    
    # Test case 6: Two elements
    height6 = [1, 2]
    assert solution.trap(height6) == 0
    assert solution.trap_dp(height6) == 0
    
    # Test case 7: Valley shape
    height7 = [5, 0, 5]
    assert solution.trap(height7) == 5
    assert solution.trap_dp(height7) == 5
    
    print("All tests passed!")