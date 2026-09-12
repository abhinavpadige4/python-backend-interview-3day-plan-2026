"""
142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/

Given the head of a linked list, return the node where the cycle begins. 
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of the 
node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. 
Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Detect the node where a cycle begins in a linked list using Floyd's algorithm.
        
        Time Complexity: O(n) - we traverse the list at most twice
        Space Complexity: O(1) - we only use two pointers
        
        Args:
            head: Head of the linked list
            
        Returns:
            The node where the cycle begins, or None if there is no cycle
        """
        if not head or not head.next:
            return None
        
        # Phase 1: Detect if there's a cycle using Floyd's Tortoise and Hare
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:  # Cycle detected
                break
        else:
            # No cycle found
            return None
        
        # Phase 2: Find the start of the cycle
        # Move one pointer to head and keep the other at meeting point
        # Move both at same speed, they'll meet at cycle start
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow  # or fast, they're equal


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


def linked_list_to_list_with_cycle_check(head, max_steps=100):
    """
    Convert linked list to list, detecting cycles to prevent infinite loops.
    
    Args:
        head: Head of the linked list
        max_steps: Maximum steps to prevent infinite loop
        
    Returns:
        List of values and boolean indicating if cycle was detected
    """
    result = []
    visited = set()
    current = head
    steps = 0
    
    while current and steps < max_steps:
        if id(current) in visited:
            return result, True  # Cycle detected
        visited.add(id(current))
        result.append(current.val)
        current = current.next
        steps += 1
    
    return result, False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Cycle at position 1
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    cycle_start1 = solution.detectCycle(head1)
    assert cycle_start1 is not None
    assert cycle_start1.val == 2  # Node at index 1
    
    # Test case 2: Cycle at position 0
    head2 = create_linked_list_with_cycle([1, 2], 0)
    cycle_start2 = solution.detectCycle(head2)
    assert cycle_start2 is not None
    assert cycle_start2.val == 1  # Node at index 0
    
    # Test case 3: No cycle
    head3 = create_linked_list_with_cycle([1], -1)
    cycle_start3 = solution.detectCycle(head3)
    assert cycle_start3 is None
    
    # Test case 4: Empty list
    head4 = create_linked_list_with_cycle([], -1)
    cycle_start4 = solution.detectCycle(head4)
    assert cycle_start4 is None
    
    # Test case 5: Single node with cycle to itself
    head5 = create_linked_list_with_cycle([1], 0)
    cycle_start5 = solution.detectCycle(head5)
    assert cycle_start5 is not None
    assert cycle_start5.val == 1
    
    # Test case 6: Larger list with cycle in middle
    head6 = create_linked_list_with_cycle([1, 2, 3, 4, 5], 2)
    cycle_start6 = solution.detectCycle(head6)
    assert cycle_start6 is not None
    assert cycle_start6.val == 3  # Node at index 2
    
    print("All tests passed!")