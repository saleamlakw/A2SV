# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,ans):
        if not root:
            return (0,0)
        left=self.dfs(root.left,ans)
        right=self.dfs(root.right,ans)
        total=left[1]+right[1]+root.val
        size=left[0]+right[0]+1
        if total//size==root.val:
            ans[0]+=1
        return (size,total)
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        self.dfs(root,ans)
        return ans[0]
        