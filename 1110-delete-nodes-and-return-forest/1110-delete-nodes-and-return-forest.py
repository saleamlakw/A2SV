# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete=set(to_delete)
        q=deque([[root,False]])
        result=[]
        while q:
            for _ in range(len(q)):
                node,fam=q.popleft()
                if node.val in to_delete:
                    fam=False
                else:
                    if not fam:
                        result.append(node)
                    fam=True
                
                if node.left:
                    q.append([node.left,fam])
                    if node.left.val in to_delete:
                        node.left=None
                
                if node.right:
                    q.append([node.right,fam])
                    if node.right.val in to_delete:
                        node.right=None
        return result
                

