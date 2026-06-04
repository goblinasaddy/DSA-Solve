# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q=collections.deque([root])
        while q:
            e=q.popleft()
            e.left,e.right=e.right,e.left

            if e.left:
                q.append(e.left)
            if e.right:
                q.append(e.right)

        return root
