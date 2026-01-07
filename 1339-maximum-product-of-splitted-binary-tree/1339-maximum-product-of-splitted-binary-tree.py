# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        tot = 0

        def dfs(node):
            nonlocal ans,tot
            if not node:
                return 0
            left = right = 0
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            cutted = node.val + left + right 
            remainig = tot - cutted 
            ans = max(ans,remainig * cutted)
            return cutted
        tot = dfs(root)
        dfs(root)
        MOD = 10**9+7
        return ans % MOD
        
            