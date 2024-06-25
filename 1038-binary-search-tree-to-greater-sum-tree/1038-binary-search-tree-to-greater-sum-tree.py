# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nodes=[]
        
        def inorder(node):
            if not node:
                return 
            
            left=inorder(node.left)
            nodes.append(node.val)
            right=inorder(node.right)
        inorder(root)
        # print(nodes)
        hashmap=Counter()
        tot=sum(nodes)
        acc=0
        for ele in nodes:
            hashmap[ele]=acc
            acc+=ele
        # print(hashmap)
        
        def inorder(node):
            if not node:
                return 
            
            left=inorder(node.left)
            node.val=tot-hashmap[node.val]
            right=inorder(node.right)

        inorder(root)
        return root