# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,arr):
        if not root:
            arr.append(0)
            return 
        arr.append(root.val)
        self.preorder(root.left,arr)
        self.preorder(root.right,arr)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ap=[]
        aq=[]
        pp=self.preorder(p,ap)
        qq=self.preorder(q,aq)
        if len(ap)!=len(aq):
            return False
        else:
            for i in range(len(ap)):
                if ap[i]!=aq[i]:
                    return False
        return True
        
        
        