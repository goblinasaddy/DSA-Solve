# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def solve(root):
            nonlocal diameter


            if not root:
                return 0

            lh = solve(root.left)
            rh = solve(root.right)

            diameter = max(diameter,lh+rh)

            return 1+max(lh,rh)
        solve(root)
        return diameter