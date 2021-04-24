# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def sumEvenGrandparent(self, root):
    nodes = [root]
    total = 0

    while nodes:
        currentNode = nodes.pop()
        
        if hasattr(currentNode, 'parent') and hasattr(currentNode.parent, 'parent'):
                if currentNode.parent.parent.val % 2 == 0:
                    total += currentNode.val
        
        if currentNode.right:
            currentNode.right.parent = currentNode
            nodes.append(currentNode.right)
        if currentNode.left:
            currentNode.left.parent = currentNode
            nodes.append(currentNode.left)
    
    return total

# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

# If there are no nodes with an even-valued grandparent, return 0.

 

# Example 1:

# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

 

# Constraints:

#     The number of nodes in the tree is between 1 and 10^4.
#     The value of nodes is between 1 and 100.
