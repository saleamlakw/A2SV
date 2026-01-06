# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        max_ = float("-inf")
        max_level = 0
        level = 1
        while queue:
            sum_= 0
            for _ in range(len(queue)):
                node = queue.popleft()
                sum_ += node.val
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sum_ > max_:
                max_ = sum_
                max_level = level
            level += 1
        return max_level
                