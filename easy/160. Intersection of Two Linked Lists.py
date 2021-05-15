# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    A_nodes = {}
    current_node_A = headA
    current_node_B = headB

    while current_node_A:
        if current_node_A.val in A_nodes:
            A_nodes[current_node_A.val].append(current_node_A)
        else:
            A_nodes[current_node_A.val] = [current_node_A]

        current_node_A = current_node_A.next

    while current_node_B:
        B_val = current_node_B.val

        if B_val in A_nodes:
            if type(A_nodes[B_val]) == list:
                for el in A_nodes[B_val]:
                    if el == current_node_B:
                        return el

        current_node_B = current_node_B.next