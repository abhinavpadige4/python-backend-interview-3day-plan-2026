"""
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', it cannot satisfy the requirement.

Constraints:
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Find the minimum window substring using sliding window technique.
        
        Time Complexity: O(m + n) - we traverse s with two pointers and t once
        Space Complexity: O(m + n) - we store character counts
        
        Args:
            s: Source string
            t: Target string containing characters to include
            
        Returns:
            Minimum window substring or empty string if not found
        """
        if not s or not t or len(s) < len(t):
            return ""
        
        # Count characters in t
        t_count = Counter(t)
        required = len(t_count)
        
        # Sliding window variables
        left = 0
        right = 0
        formed = 0
        window_counts = {}
        
        # Result variables
        min_length = float('inf')
        min_left = 0
        min_right = 0
        
        # Expand the window
        while right < len(s):
            # Add character from the right
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if current character's count matches required count
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            
            # Try to contract the window till it ceases to be desirable
            while left <= right and formed == required:
                char = s[left]
                
                # Update minimum window if this is smaller
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left
                    min_right = right
                
                # Remove character from left
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if min_length == float('inf') else s[min_left:min_right + 1]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Normal case
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    assert solution.minWindow(s1, t1) == "BANC"
    
    # Test case 2: Single character match
    s2 = "a"
    t2 = "a"
    assert solution.minWindow(s2, t2) == "a"
    
    # Test case 3: Not enough characters
    s3 = "a"
    t3 = "aa"
    assert solution.minWindow(s3, t3) == ""
    
    # Test case 4: Multiple same characters
    s4 = "aa"
    t4 = "aa"
    assert solution.minWindow(s4, t4) == "aa"
    
    # Test case 5: Characters in different order
    s5 = "ab"
    t5 = "b"
    assert solution.minWindow(s5, t5) == "b"
    
    # Test case 6: No match
    s6 = "abcd"
    t6 = "ef"
    assert solution.minWindow(s6, t6) == ""
    
    # Test case 7: Complex case
    s7 = "abbbbbcba"
    t7 = "bc"
    assert solution.minWindow(s7, t7) == "cba"
    
    print("All tests passed!")