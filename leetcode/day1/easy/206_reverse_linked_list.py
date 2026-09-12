"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list iteratively.
        
        Time Complexity: O(n) - we visit each node exactly once
        Space Complexity: O(1) - we only use constant extra space
        
        Args:
            head: The head of the linked list
            
        Returns:
            The new head of the reversed linked list
        """
        prev = None
        current = head
        
        while current:
            # Store the next node
            next_temp = current.next
            # Reverse the current node's pointer
            current.next = prev
            # Move prev and current one step forward
            prev = current
            current = next_temp
            
        return prev
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list recursively.
        
        Time Complexity: O(n) - we visit each node exactly once
        Space Complexity: O(n) - due to recursion stack
        
        Args:
            head: The head of the linked list
            
        Returns:
            The new head of the reversed linked list
        """
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest of the list
        new_head = self.reverseListRecursive(head.next)
        # Put the first element at the end
        head.next.next = head
        head.next = None
        
        return new_head


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
    
    # Test case 1: Normal list
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = solution.reverseList(head1)
    assert linked_list_to_list(reversed1) == [5, 4, 3, 2, 1]
    
    # Test case 2: Two elements
    head2 = create_linked_list([1, 2])
    reversed2 = solution.reverseList(head2)
    assert linked_list_to_list(reversed2) == [2, 1]
    
    # Test case 3: Empty list
    head3 = create_linked_list([])
    reversed3 = solution.reverseList(head3)
    assert linked_list_to_list(reversed3) == []
    
    # Test case 4: Single element
    head4 = create_linked_list([1])
    reversed4 = solution.reverseList(head4)
    assert linked_list_to_list(reversed4) == [1]
    
    # Test recursive version
    head5 = create_linked_list([1, 2, 3, 4, 5])
    reversed5 = solution.reverseListRecursive(head5)
    assert linked_list_to_list(reversed5) == [5, 4, 3, 2, 1]
    
    print("All tests passed!")