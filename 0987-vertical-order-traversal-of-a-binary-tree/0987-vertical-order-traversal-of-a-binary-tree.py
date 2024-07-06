# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        def inorder(node,r,c):
            if not node:
                return 
            inorder(node.left,r+1,c-1)
            result.append([c,r,node.val])
            inorder(node.right,r+1,c+1)
        inorder(root,0,0)
        result.sort()
        cc=defaultdict(list)
        prev=result[0][0]
        i=0
        re=[[]]
        for ele in result:
            if ele[0]!=prev:
                re.append([])
            prev=ele[0]
            re[-1].append(ele[-1])
        return re
        