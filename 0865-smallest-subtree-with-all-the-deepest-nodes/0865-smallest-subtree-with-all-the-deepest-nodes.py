# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def deepest(root):
            def dfs(node):
                if not node:
                    return 0
                left=1+dfs(node.left)
                right=1+dfs(node.right)
                return max(left, right)
            return dfs(root)
        
        depth=deepest(root)-1
      
        def collect(root,depth):
            arr=[]
            def dfs(node,dep):
                if not node:
                    return 
                if dep==depth:
                    arr.append(node)
                dfs(node.left,dep+1)
                dfs(node.right,dep+1)
            dfs(root,0)
            return arr
        
        arr=collect(root,depth)
       
        def lca(root, p , q):
            def dfs(node):
                if not node:
                    return None
                if node.val==p.val:
                    return p
                if node.val==q.val:
                    return q
                
                left=dfs(node.left)
                right=dfs(node.right)
                if left and not right:
                    return left
                if right and not left:
                    return right 
                if left and right:
                    return node
            return dfs(root)
        
        pre=arr[0]
        for nd in arr:
            pre=lca(root,pre,nd)
        return pre