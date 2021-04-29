# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        current_node = head

        while current_node:
            nodes.append(current_node.val)
            current_node = current_node.next

        return nodes == list(reversed(nodes))

# Given the head of a singly linked list, return true if it is a palindrome.

 

# Example 1:

# Input: head = [1,2,2,1]
# Output: true

# Example 2:

# Input: head = [1,2]
# Output: false

 

# Constraints:

#     The number of nodes in the list is in the range [1, 105].
#     0 <= Node.val <= 9

# Follow up: Could you do it in O(n) time and O(1) space?