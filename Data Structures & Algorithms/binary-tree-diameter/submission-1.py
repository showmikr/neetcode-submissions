# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def depth(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            res = max(res, left_depth + right_depth)
            return max(left_depth, right_depth) + 1
        depth(root)
        return res

    
