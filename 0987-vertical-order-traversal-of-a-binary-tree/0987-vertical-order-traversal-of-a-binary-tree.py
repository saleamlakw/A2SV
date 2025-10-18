# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        verticalOrder = defaultdict(list)
        minCol = float("inf")
        maxCol = float("-inf")
        def dfs(node,r,c):
            nonlocal minCol , maxCol
            if not node :
                return 
            minCol = min(minCol,c)
            maxCol = max(maxCol,c)
            verticalOrder[c].append((r,node.val))
            
            dfs(node.left , r+1, c-1)
            dfs(node.right , r+1, c+1)
        dfs(root,0,0)
        ans = []
        for col in range(minCol , maxCol+1):
            ans.append( [y for x,y in sorted(verticalOrder[col])])

        return ans
