"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of the 
node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect if a linked list has a cycle using Floyd's Tortoise and Hare algorithm.
        
        Time Complexity: O(n) - in worst case, we traverse the list once
        Space Complexity: O(1) - we only use two pointers
        
        Args:
            head: The head of the linked list
            
        Returns:
            True if there is a cycle, False otherwise
        """
        if not head or not head.next:
            return False
        
        # Initialize slow and fast pointers
        slow = head
        fast = head.next
        
        # Traverse the list
        while slow != fast:
            # If we reach the end, there's no cycle
            if not fast or not fast.next:
                return False
            slow = slow.next          # Move slow by 1 step
            fast = fast.next.next     # Move fast by 2 steps
        
        # If they meet, there's a cycle
        return True


# Helper functions for testing
def create_linked_list_with_cycle(values, pos):
    """
    Create a linked list with a cycle at the specified position.
    
    Args:
        values: List of node values
        pos: Position (0-indexed) where tail connects to, -1 for no cycle
        
    Returns:
        Head of the linked list
    """
    if not values:
        return None
    
    # Create all nodes
    nodes = [ListNode(val) for val in values]
    
    # Link nodes together
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Create cycle if pos is valid
    if pos != -1 and pos < len(nodes):
        nodes[-1].next = nodes[pos]
    
    return nodes[0] if nodes else None


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: List with cycle at position 1
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    assert solution.hasCycle(head1) == True
    
    # Test case 2: List with cycle at position 0
    head2 = create_linked_list_with_cycle([1, 2], 0)
    assert solution.hasCycle(head2) == True
    
    # Test case 3: List without cycle
    head3 = create_linked_list_with_cycle([1], -1)
    assert solution.hasCycle(head3) == False
    
    # Test case 4: Empty list
    head4 = create_linked_list_with_cycle([], -1)
    assert solution.hasCycle(head4) == False
    
    # Test case 5: Single node without cycle
    head5 = create_linked_list_with_cycle([1], -1)
    assert solution.hasCycle(head5) == False
    
    # Test case 6: Single node with cycle to itself
    head6 = create_linked_list_with_cycle([1], 0)
    assert solution.hasCycle(head6) == True
    
    print("All tests passed!")