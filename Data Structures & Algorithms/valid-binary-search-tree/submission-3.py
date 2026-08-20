from itertools import chain
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidHelper(root: Optional[TreeNode], lower_bound: int, upper_bound: int) -> bool:
            if not root:
                return True
            if not (lower_bound < root.val < upper_bound):
                return False
            is_left_bst = isValidHelper(root.left, lower_bound, root.val)
            is_right_bst = isValidHelper(root.right, root.val, upper_bound)
            return is_left_bst and is_right_bst
        return isValidHelper(root, -float('inf'), float('inf'))
        