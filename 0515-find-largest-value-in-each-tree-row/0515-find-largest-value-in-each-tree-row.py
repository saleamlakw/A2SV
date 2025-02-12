# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        qu=deque()
        re=[]
        qu.append(root)
        arr=[]
        arr.append(root.val)
        while qu:
            re.append(max(arr))
            for i in range(len(qu)):
                curr=qu.popleft()
                arr.pop(0)
                if curr.left:
                    qu.append(curr.left)
                    arr.append(curr.left.val)
                if curr.right:
                    qu.append(curr.right)
                    arr.append(curr.right.val)
        return re