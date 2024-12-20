# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        level = 0
        def reverse(queue):
            left = 0
            right = len(queue)-1
            while right > left:
                queue[left].val , queue[right].val = queue[right].val , queue[left].val
                left += 1
                right -= 1
            
        while queue:
            if level % 2:
                reverse(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return root
            