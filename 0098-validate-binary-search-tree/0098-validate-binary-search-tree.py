# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,arr):
        if not root:
            return 
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr=[]
        self.inorder(root,arr)
        for i in range(1,len(arr)):
            if arr[i-1]>=arr[i]:
                return False
        return True
    
        