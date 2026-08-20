# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        res = []
        while queue:
            temp = [n.val for n in queue if n]
            if temp:
                res.append(temp)
            next_level = []
            for node in queue:
                if not node:
                    continue
                next_level.extend(n for n in [node.left, node.right] if n)
            queue = next_level
        return res
            