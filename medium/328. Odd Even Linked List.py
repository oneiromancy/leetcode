# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        node_idx = 1
        current_node = head
        previous_node = None
        last_odd_node = None

        while current_node:
            if node_idx % 2 == 0:
                previous_node = current_node
                current_node = current_node.next
            else:
                if previous_node is None:
                    previous_node = last_odd_node = current_node
                    current_node = current_node.next
                elif last_odd_node is None:
                    next_node = current_node.next

                    # attaching it as the head
                    current_node.next = head
                    last_odd_node = current_node
                    head = current_node

                    # removing odd node by skipping to the next
                    previous_node.next = current_node = next_node
                else:
                    next_node = current_node.next

                    # attaching it to the right of odd nodes
                    current_node.next = last_odd_node.next
                    last_odd_node.next = current_node
                    last_odd_node = current_node

                    # removing odd node by skipping to the next
                    previous_node.next = current_node = next_node

            node_idx += 1
                

        return head

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

 

# Example 1:

# Input: head = [1,2,3,4,5] => [1, 2, 3, 4, 5]
# Output: [1,3,5,2,4]

# Example 2:

# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]

 

# Constraints:

#     The number of nodes in the linked list is in the range [0, 104].
#     -106 <= Node.val <= 106

 
# Follow up: Could you solve it in O(1) space complexity and O(nodes) time complexity?