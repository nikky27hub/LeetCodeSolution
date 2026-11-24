# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        from collections import deque

        q = deque([root])
        max_sum = float('-inf')
        ans = 1
        level = 1

        while q:
            total = 0

            for _ in range(len(q)):
                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if total > max_sum:
                max_sum = total
                ans = level

            level += 1

        return ans
        