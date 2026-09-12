"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= n <= sz
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of a linked list using two pointers.
        
        Time Complexity: O(L) - we make one pass through the list
        Space Complexity: O(1) - we only use two pointers
        
        Args:
            head: Head of the linked list
            n: Position from the end to remove (1-indexed)
            
        Returns:
            Head of the modified linked list
        """
        # Create a dummy node to handle edge cases (like removing the head)
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Move right pointer n steps ahead
        for _ in range(n):
            right = right.next
        
        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next
        
        # Skip the nth node from the end
        left.next = left.next.next
        
        return dummy.next


# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values and return the head."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Convert a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Remove 2nd from end
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.removeNthFromEnd(head1, 2)
    assert linked_list_to_list(result1) == [1, 2, 3, 5]
    
    # Test case 2: Remove 1st from end (last element) from single node list
    head2 = create_linked_list([1])
    result2 = solution.removeNthFromEnd(head2, 1)
    assert linked_list_to_list(result2) == []
    
    # Test case 3: Remove 1st from end from two-node list
    head3 = create_linked_list([1, 2])
    result3 = solution.removeNthFromEnd(head3, 1)
    assert linked_list_to_list(result3) == [1]
    
    # Test case 4: Remove sz-th from end (first element)
    head4 = create_linked_list([1, 2, 3, 4, 5])
    result4 = solution.removeNthFromEnd(head4, 5)
    assert linked_list_to_list(result4) == [2, 3, 4, 5]
    
    # Test case 5: Remove from middle
    head5 = create_linked_list([1, 2, 3, 4, 5])
    result5 = solution.removeNthFromEnd(head5, 3)
    assert linked_list_to_list(result5) == [1, 2, 4, 5]
    
    print("All tests passed!")