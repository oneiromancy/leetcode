# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l = []
        self.inorder(root, l, k)
        return l[k-1]

    def inorder(self, root, l, k):
        if root and len(l) < k:
            self.inorder(root.left, l, k)
            l.append(root.val)
            self.inorder(root.right, l, k)

        return l

# Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

 

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

 

# Constraints:

#     The number of nodes in the tree is n.
#     1 <= k <= n <= 104
#     0 <= Node.val <= 104

 
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?