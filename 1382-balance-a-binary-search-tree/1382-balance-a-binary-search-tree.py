class Solution:
    def balanceBST(self, root):
        
        def dfs(node):
            if not node: return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        ns = dfs(root)
        
        def build(l, r):
            if l > r: return None
            m = (l + r) // 2
            root = TreeNode(ns[m])
            root.left, root.right = build(l, m-1), build(m + 1, r)
            return root
        
        return build(0, len(ns) - 1)