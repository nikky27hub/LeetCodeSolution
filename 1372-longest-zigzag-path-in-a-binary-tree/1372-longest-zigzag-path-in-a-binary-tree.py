# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        self.ans = 0

        def dfs(node, left, right):
            if not node:
                return

            self.ans = max(self.ans, left, right)

            # Move left: next move must be right
            dfs(node.left, right + 1, 0)

            # Move right: next move must be left
            dfs(node.right, 0, left + 1)

        dfs(root, 0, 0)
        return self.ans

        