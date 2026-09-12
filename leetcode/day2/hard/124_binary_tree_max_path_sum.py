"""
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence 
has an edge connecting them. No node can appear in the sequence more than once. 
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -1000 <= Node.val <= 1000
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum path sum in a binary tree using DFS.
        
        Time Complexity: O(n) - we visit each node exactly once
        Space Complexity: O(h) - where h is the height of the tree (recursion stack)
        
        Args:
            root: Root of the binary tree
            
        Returns:
            Maximum path sum of any non-empty path
        """
        self.max_sum = float('-inf')  # Initialize to negative infinity
        
        def max_gain(node):
            """
            Calculate the maximum gain from a node.
            The gain is the maximum sum of the path starting from this node 
            going down to any leaf in its subtree.
            """
            if not node:
                return 0
            
            # Recursively calculate the maximum gain from left and right subtrees
            # If the gain is negative, we ignore it (take 0 instead)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Price to start a new path where 'node' is the highest point
            price_new_path = node.val + left_gain + right_gain
            
            # Update the global maximum sum
            self.max_sum = max(self.max_sum, price_new_path)
            
            # For recursion, return the maximum gain if we continue the same path
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum


# Helper functions for testing
def create_binary_tree(values):
    """
    Create a binary tree from a list of values (level-order traversal).
    None represents absent nodes.
    
    Args:
        values: List of values in level-order (None for missing nodes)
        
    Returns:
        Root of the binary tree
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Simple tree
    #     1
    #    / \
    #   2   3
    root1 = create_binary_tree([1, 2, 3])
    assert solution.maxPathSum(root1) == 6
    
    # Test case 2: More complex tree
    #     -10
    #     / \
    #    9  20
    #       / \
    #      15  7
    root2 = create_binary_tree([-10, 9, 20, None, None, 15, 7])
    assert solution.maxPathSum(root2) == 42
    
    # Test case 3: Single node
    root3 = create_binary_tree([5])
    assert solution.maxPathSum(root3) == 5
    
    # Test case 4: All negative values
    #    -2
    #    / \
    #  -1  -3
    root4 = create_binary_tree([-2, -1, -3])
    assert solution.maxPathSum(root4) == -1  # Just the node with value -1
    
    # Test case 5: Linear tree (like a linked list)
    #   1
    #    \
    #     2
    #      \
    #       3
    root5 = create_binary_tree([1, None, 2, None, None, None, 3])
    assert solution.maxPathSum(root5) == 6  # 1 + 2 + 3
    
    # Test case 6: Mixed positive and negative
    #     1
    #    / \
    #   2   -3
    #  / \   
    # 4   5
    root6 = create_binary_tree([1, 2, -3, 4, 5])
    assert solution.maxPathSum(root6) == 12  # 4 + 2 + 1 + 5
    
    print("All tests passed!")