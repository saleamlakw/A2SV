# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q=deque([root])
        va=deque([root])
        result=[]
        while q:
            if len(set(va))!=1:
                return False
            for _ in range(len(q)):
                node=q.popleft()
                va.popleft()
                if node.left:
                    q.append(node.left)
                    va.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    va.append(node.right.val)
            
        return True