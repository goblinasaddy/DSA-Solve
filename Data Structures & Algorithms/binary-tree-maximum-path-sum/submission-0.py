# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = -1000000000
        def solve(root):
            nonlocal maxi

            if not root:
                return 0

            ls = solve(root.left)
            if ls<0:
                ls = 0
            rs = solve(root.right)
            if rs<0:
                rs = 0
            maxi = max(maxi,ls+root.val+rs)
            return root.val+max(ls,rs)

        solve(root)
        return maxi