# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l2_nodes = []
        current_l2 = l2

        while current_l2:
            l2_nodes.append(current_l2)
            current_l2 = current_l2.next

        prev_l1 = None
        current_l1 = l1
        counter = 0
        
        while current_l1 and counter < len(l2_nodes):
            current_l2 = l2_nodes[counter]

            if current_l2.val <= current_l1.val:
                current_l2.next = current_l1
                
                if prev_l1:
                    prev_l1.next = current_l2
                    prev_l1 = prev_l1.next
                else:
                    l1 = current_l2
                    prev_l1 = current_l2
                counter += 1
            else:
                prev_l1 = current_l1
                current_l1 = current_l1.next
        
        if counter < len(l2_nodes) and l1:
            prev_l1.next = l2_nodes[counter]
        elif not l1:
            l1 = l2


        return l1

        
            
            



# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]