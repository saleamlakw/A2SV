# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,low,high,re):
        if not root:
            return None
        if root.val>=low and root.val<=high:
            re.append(root.val)
        self.preorder(root.left,low,high,re)
        self.preorder(root.right,low,high,re)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        re=[]
        self.preorder(root,low,high,re)
        return sum(re)
        