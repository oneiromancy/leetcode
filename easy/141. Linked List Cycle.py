# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes = {}
        current_node = head
        
        while current_node:
            if current_node not in nodes:
                nodes[current_node] = True
            else:
                return True

            current_node = current_node.next
