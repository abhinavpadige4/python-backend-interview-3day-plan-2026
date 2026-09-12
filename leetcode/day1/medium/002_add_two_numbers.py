"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented by linked lists in reverse order.
        
        Time Complexity: O(max(m, n)) - we traverse the longer list once
        Space Complexity: O(max(m, n)) - the length of the new list is at most max(m,n) + 1
        
        Args:
            l1: Head of the first linked list
            l2: Head of the second linked list
            
        Returns:
            Head of the linked list representing the sum
        """
        dummy_head = ListNode()
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            # Get the current digits (0 if list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_head.next


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
    
    # Test case 1: Normal case
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [7, 0, 8]
    
    # Test case 2: Both zeros
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [0]
    
    # Test case 3: Different lengths with carry
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]
    
    # Test case 4: One list longer
    l1 = create_linked_list([1, 8])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [1, 8]
    
    # Test case 5: Carry propagates through
    l1 = create_linked_list([9, 9])
    l2 = create_linked_list([1])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [0, 0, 1]
    
    print("All tests passed!")