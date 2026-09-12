"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together 
the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted list.
        
        Time Complexity: O(n + m) - we visit each node in both lists exactly once
        Space Complexity: O(1) - we only rearrange existing nodes, no new nodes created
        
        Args:
            list1: Head of the first sorted linked list
            list2: Head of the second sorted linked list
            
        Returns:
            Head of the merged sorted linked list
        """
        # Create a dummy node to serve as the start of the result list
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists until we reach the end of one
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach the remaining part of the non-empty list
        current.next = list1 if list1 else list2
        
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
    
    # Test case 1: Both lists have elements
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 1, 2, 3, 4, 4]
    
    # Test case 2: Both lists empty
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == []
    
    # Test case 3: First list empty, second has elements
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [0]
    
    # Test case 4: Second list empty, first has elements
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 2, 3]
    
    # Test case 5: Lists with different lengths
    list1 = create_linked_list([1, 3, 5, 7])
    list2 = create_linked_list([2, 4, 6])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 2, 3, 4, 5, 6, 7]
    
    print("All tests passed!")