"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.
"""

from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists using a min-heap.
        
        Time Complexity: O(N log k) - where N is total number of nodes
                        Each heap operation takes O(log k) and we do N operations
        Space Complexity: O(k) - the heap can contain at most k elements
        
        Args:
            lists: List of k sorted linked lists
            
        Returns:
            Head of the merged sorted linked list
        """
        if not lists or all(l is None for l in lists):
            return None
        
        # Create a min-heap
        heap = []
        
        # Push the first node of each list into the heap
        # We use (value, list_index, node) to handle duplicate values
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))
        
        # Create dummy head for the result list
        dummy = ListNode()
        current = dummy
        
        # Extract the smallest element and add the next node from its list
        while heap:
            val, list_idx, node = heapq.heappop(heap)
            
            # Add the smallest node to the result
            current.next = ListNode(val)
            current = current.next
            
            # If there's a next node in the same list, add it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
        
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
    
    # Test case 1: Normal case with three lists
    lists1 = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    result1 = solution.mergeKLists(lists1)
    assert linked_list_to_list(result1) == [1, 1, 2, 3, 4, 4, 5, 6]
    
    # Test case 2: Empty input
    lists2 = []
    result2 = solution.mergeKLists(lists2)
    assert result2 is None
    
    # Test case 3: List with empty list
    lists3 = [[]]
    result3 = solution.mergeKLists(lists3)
    assert result3 is None
    
    # Test case 4: Single list
    lists4 = [create_linked_list([1, 2, 3])]
    result4 = solution.mergeKLists(lists4)
    assert linked_list_to_list(result4) == [1, 2, 3]
    
    # Test case 5: Two lists
    lists5 = [
        create_linked_list([1, 3, 5]),
        create_linked_list([2, 4, 6])
    ]
    result5 = solution.mergeKLists(lists5)
    assert linked_list_to_list(result5) == [1, 2, 3, 4, 5, 6]
    
    # Test case 6: Lists with duplicates
    lists6 = [
        create_linked_list([1, 1, 2]),
        create_linked_list([1, 2, 3])
    ]
    result6 = solution.mergeKLists(lists6)
    assert linked_list_to_list(result6) == [1, 1, 1, 2, 2, 3]
    
    print("All tests passed!")