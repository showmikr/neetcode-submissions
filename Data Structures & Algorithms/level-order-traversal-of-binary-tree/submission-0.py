# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = [[root.val]]
        while queue:
            next_level = []
            for node in queue:
                next_level.extend(n for n in [node.left, node.right] if n)
            if next_level:
                res.append([n.val for n in next_level])
            queue = next_level
        return res
            