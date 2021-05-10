# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None
        curr_node = head
        
        while curr_node:
            cp_curr_node = copy.deepcopy(curr_node)
            cp_curr_node.next = prev_node
            prev_node = cp_curr_node
            
            curr_node = curr_node.next
            
        return prev_node

# N1 => N2 => N3 => ... => Ni
# N1 <= N2 <= N3 <= ... <= Ni


# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:

# Input: head = [1,2]
# Output: [2,1]

# Example 3:

# Input: head = []
# Output: []

 

# Constraints:

#     The number of nodes in the list is the range [0, 5000].
#     -5000 <= Node.val <= 5000

 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
