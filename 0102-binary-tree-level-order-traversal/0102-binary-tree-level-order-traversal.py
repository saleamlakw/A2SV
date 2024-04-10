# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        visited=set([root.val]) if root else set()
        queue=deque([root]) if root else deque()
        result=[[root.val]] if root else []
        while queue:
            re=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                    re.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    re.append(node.right.val)
            if re:
                result.append(re[:])
        return result

