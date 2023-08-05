# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict
    def preorder(self,root,dic):
        if not root:
            return None
        dic[root.val].append(root.val)
        self.preorder(root.left,dic)
        self.preorder(root.right,dic)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=defaultdict(list)
        self.preorder(root,dic)
        mx=list(map(lambda x: len(x),list(dic.values())))
        print(mx)
        return [i for i in dic if len(dic[i])==max(mx)] 
        
        