# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        nodes_by_level = [[root.val]]
        node_tracker = [(1, root.left, root.right)]
        
        while node_tracker:
            level, left, right = node_tracker.pop(0)
            
            if level % 2 == 0:
                if right:
                    node_tracker.append((level + 1, right.left, right.right))

                    if level > len(nodes_by_level) - 1:
                        nodes_by_level.append([right.val])
                    else:
                        nodes_by_level[level].insert(0, right.val)
                        
                if left:
                    node_tracker.append((level + 1, left.left, left.right))

                    if level > len(nodes_by_level) - 1:
                        nodes_by_level.append([left.val])
                    else:
                        nodes_by_level[level].insert(0, left.val)

            else:
                if right:
                    node_tracker.append((level + 1, right.left, right.right))

                    if level > len(nodes_by_level) - 1:
                        nodes_by_level.append([right.val])
                    else:
                        nodes_by_level[level].append(right.val)
                        
                if left:
                    node_tracker.append((level + 1, left.left, left.right))

                    if level > len(nodes_by_level) - 1:
                        nodes_by_level.append([left.val])
                    else:
                        nodes_by_level[level].append(left.val)

        return nodes_by_level