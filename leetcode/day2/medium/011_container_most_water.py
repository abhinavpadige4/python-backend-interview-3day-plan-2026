"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container 
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Find the container with the most water using two-pointer technique.
        
        Time Complexity: O(n) - we make one pass through the array
        Space Complexity: O(1) - we only use two pointers
        
        Args:
            height: List of integers representing line heights
            
        Returns:
            Maximum area of water that can be contained
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Update max area if current is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            # This is because moving the taller line won't increase the area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Normal case
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert solution.maxArea(height1) == 49
    
    # Test case 2: Two elements
    height2 = [1, 1]
    assert solution.maxArea(height2) == 1
    
    # Test case 3: Ascending order
    height3 = [1, 2, 3, 4, 5]
    assert solution.maxArea(height3) == 6  # Between 2 and 5: width=3, height=2
    
    # Test case 4: Descending order
    height4 = [5, 4, 3, 2, 1]
    assert solution.maxArea(height4) == 6  # Between 5 and 3: width=2, height=3
    
    # Test case 5: All same height
    height5 = [5, 5, 5, 5]
    assert solution.maxArea(height5) == 15  # Between first and last: width=3, height=5
    
    # Test case 6: One very tall line
    height6 = [1, 100, 1, 1, 1, 1, 1]
    assert solution.maxArea(height6) == 6  # Between 100 and last 1: width=5, height=1
    
    print("All tests passed!")