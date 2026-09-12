"""
84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/

Given an array of integers heights representing the histogram's bar height where the width 
of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram with width of 6.
The largest rectangle is shown in the red area, which has an area of 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Find the largest rectangle in a histogram using stack-based approach.
        
        Time Complexity: O(n) - each bar is pushed and popped from stack at most once
        Space Complexity: O(n) - the stack can store up to n elements
        
        Args:
            heights: List of integers representing bar heights
            
        Returns:
            Area of the largest rectangle in the histogram
        """
        # Add sentinel values at both ends to simplify edge cases
        heights = [0] + heights + [0]
        stack = []  # Stack to store indices
        max_area = 0
        
        for i, h in enumerate(heights):
            # While current height is less than height at stack top
            while stack and heights[stack[-1]] > h:
                # Pop the top
                height = heights[stack.pop()]
                # Width is current index minus new stack top minus 1
                width = i - stack[-1] - 1
                # Calculate area
                area = height * width
                max_area = max(max_area, area)
            
            stack.append(i)
        
        return max_area
    
    def largestRectangleArea_brute_force(self, heights: List[int]) -> int:
        """
        Find the largest rectangle in a histogram using brute force.
        
        Time Complexity: O(n^2) - nested loops
        Space Complexity: O(1) - constant extra space
        
        Args:
            heights: List of integers representing bar heights
            
        Returns:
            Area of the largest rectangle in the histogram
        """
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            min_height = heights[i]
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                area = min_height * (j - i + 1)
                max_area = max(max_area, area)
        
        return max_area


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Normal case
    heights1 = [2, 1, 5, 6, 2, 3]
    assert solution.largestRectangleArea(heights1) == 10
    assert solution.largestRectangleArea_brute_force(heights1) == 10
    
    # Test case 2: Two elements
    heights2 = [2, 4]
    assert solution.largestRectangleArea(heights2) == 4
    assert solution.largestRectangleArea_brute_force(heights2) == 4
    
    # Test case 3: All same height
    heights3 = [3, 3, 3, 3]
    assert solution.largestRectangleArea(heights3) == 12  # 3 * 4
    assert solution.largestRectangleArea_brute_force(heights3) == 12
    
    # Test case 4: Ascending order
    heights4 = [1, 2, 3, 4, 5]
    assert solution.largestRectangleArea(heights4) == 9  # 3 * 3 (from index 2-4) or 2*4 or 1*5
    assert solution.largestRectangleArea_brute_force(heights4) == 9
    
    # Test case 5: Descending order
    heights5 = [5, 4, 3, 2, 1]
    assert solution.largestRectangleArea(heights5) == 9  # 3 * 3 (from index 0-2) or 4*2 or 5*1
    assert solution.largestRectangleArea_brute_force(heights5) == 9
    
    # Test case 6: Single element
    heights6 = [5]
    assert solution.largestRectangleArea(heights6) == 5
    assert solution.largestRectangleArea_brute_force(heights6) == 5
    
    # Test case 7: Empty array (handled by constraints, but let's check)
    heights7 = []
    # According to constraints, this shouldn't happen, but our implementation handles it
    assert solution.largestRectangleArea(heights7) == 0
    
    print("All tests passed!")